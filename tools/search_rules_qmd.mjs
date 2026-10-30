// Deliberately only the pinned QMD SDK's lexical API; no CLI hooks, models or MCP.
import {readFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
import {fileURLToPath, pathToFileURL} from 'node:url';
import {dirname, resolve} from 'node:path';

const root = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const moduleRoot = resolve(root, '.validation/qmd-runtime/node_modules/@tobilu/qmd');
if (JSON.parse(readFileSync(resolve(moduleRoot, 'package.json'), 'utf8')).version !== '2.8.3') {
  throw new Error('Expected @tobilu/qmd 2.8.3');
}
const {createStore, extractSnippet} = await import(pathToFileURL(resolve(moduleRoot, 'dist/index.js')).href);
let input = '';
for await (const chunk of process.stdin) input += chunk;
const request = JSON.parse(input);
if (!['build', 'search'].includes(request.action)) throw new Error('Unsupported action');
const store = await createStore({dbPath: request.db,
  config: {collections: {'ki-regeln': {path: request.corpus, pattern: '**/*.md'}}}});
try {
  const paths = () => store.internal.getActiveDocumentPaths('ki-regeln').sort();
  let output;
  if (request.action === 'build') {
    const result = await store.update();
    output = {paths: paths(), skipped: result.skipped};
  } else {
    if (JSON.stringify(paths()) !== JSON.stringify(request.paths)) throw new Error('Incomplete collection');
    const results = await store.searchLex(request.query, {limit: 5, collection: 'ki-regeln'});
    output = {hits: results.map(hit => {
      const prefix = 'qmd://ki-regeln/';
      if (!hit.filepath.startsWith(prefix)) throw new Error('Unexpected collection');
      return {path: hit.filepath.slice(prefix.length), score: hit.score,
        snippet: extractSnippet(hit.body, request.query, 600).snippet.slice(0, 600),
        content_sha256: createHash('sha256').update(hit.body).digest('hex')};
    })};
  }
  process.stdout.write(JSON.stringify(output));
} finally {
  await store.close();
}
