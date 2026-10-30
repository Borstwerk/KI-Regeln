"""Bounded native QMD evidence; public repository and synthetic fixtures only."""
import hashlib,json,os,pathlib,shutil,subprocess,sys,tempfile,time
from datetime import datetime,timezone
root=pathlib.Path(__file__).resolve().parents[2];sys.path.insert(0,str(root))
from tools import search_rules as search
from tools.check_public_entrypoints import PROJECT_CORE
if sys.argv[1:] != ['--run']:
    raise SystemExit('Explicit --run required; installs nothing, updates only the local derived index.')
(root/'.validation/tmp').mkdir(parents=True,exist_ok=True)
out=pathlib.Path(tempfile.mkdtemp(prefix='native-rule-search-',dir=root/'.validation'))
sha=lambda b:hashlib.sha256(b).hexdigest()
node=shutil.which('node')
revision=subprocess.check_output(['git','rev-parse','HEAD'],cwd=root,text=True).strip()
protocol={'utc':datetime.now(timezone.utc).isoformat(),'source_commit':revision,'execution_commit':revision,
    'node_version':subprocess.check_output([node,'--version'],text=True).strip(),'qmd_version':'2.8.3','mode':'bm25',
    'script_sha256':{name:sha((root/name).read_bytes()) for name in ['tools/search_rules.py','tools/search_rules_qmd.mjs','Search-KI-Regeln.ps1','tools/local_search/pnpm-lock.yaml']},
    'helper_sha256':sha(pathlib.Path(__file__).read_bytes()),'model_calls':0,'held_out':False}
cases=[('Skill Verbesserung Fehler',{'Skill-Engineering/Evidence-getriebene-Skill-Verbesserung.md','Workflows/Skill-Verbesserung-aus-Evals-und-Fehlern.md'}),
       ('Teststrategie Grenzwerte',{'Testing-und-QA/Skills/test-design/SKILL.md','Testing-und-QA/README.md'}),
       ('MCP Berechtigungen',{'Sicherheit/MCP-und-externe-Tools.md','Sicherheit/Skills/tool-permission-review/SKILL.md'}),
       ('Workflow beitragen',{'CONTRIBUTING.md','PROJECT.md'}),('zzretrievalcanaryf72ea4bd',set())]
protocol['cases']=[{'query':q,'allowed_top_five':sorted(expected),'expect_empty':not expected} for q,expected in cases]
(out/'protocol.json').write_text(json.dumps(protocol,ensure_ascii=False,indent=2),encoding='utf-8')
metadata,files=search.read_snapshot(root)
before={name:sha((root/name).read_bytes()) for name in files}
(root/'.validation/search-excluded-canary.md').write_text('zzretrievalcanaryf72ea4bd\n',encoding='utf-8')
assert not any(b'zzretrievalcanaryf72ea4bd' in body for body in files.values())
start=time.monotonic();built=search.build(root,node);elapsed=round(time.monotonic()-start,3)
results=[]
for query,expected in cases:
    start=time.monotonic();result=search.search(root,query,node);duration=round(time.monotonic()-start,3)
    paths={hit['path'] for hit in result['hits']}
    passed=bool(paths&expected) if expected else not paths
    results.append({'query':query,'pass':passed,'seconds':duration,'result':result})
    assert passed,(query,paths)
after={name:sha((root/name).read_bytes()) for name in files}
assert before==after
# Isolated real engine, with a deliberately empty selected document as a partial-index countercheck.
git_env={k:v for k,v in os.environ.items() if not k.startswith('GIT_')}
git_env.update(GIT_CONFIG_NOSYSTEM='1',GIT_CONFIG_GLOBAL=os.devnull,GIT_TERMINAL_PROMPT='0')
with tempfile.TemporaryDirectory(prefix='qmd-native-fixture-',dir=root/'.validation/tmp') as temp:
    fixture=pathlib.Path(temp)
    def git(*args):return subprocess.check_output(['git',*args],cwd=fixture,env=git_env,stderr=subprocess.PIPE)
    git('init','--quiet','--object-format=sha1');git('config','user.name','Synthetic QMD Fixture');git('config','user.email','fixture@example.invalid')
    git('config','core.autocrlf','false')
    for name in sorted(PROJECT_CORE):
        path=fixture/name;path.parent.mkdir(parents=True,exist_ok=True);path.write_text('# Synthetic source\nOnly fixture text.\n',encoding='utf-8')
    path=fixture/'docs/Überblick.md';path.parent.mkdir();path.write_text('# Übersicht\nregelcanaryeinfache\n',encoding='utf-8')
    manifest={'schema_version':1,'id':'ki-regeln','kind':'collection','entrypoints':{'overview':'PROJECT.md','contents':'START-HIER.md','status':'README.md','plan':'CONTRIBUTING.md'},'search':{'include':sorted(PROJECT_CORE|{'docs/Überblick.md'}),'exclude':[]}}
    def commit(message):
        (fixture/'mara-project.json').write_text(json.dumps(manifest,ensure_ascii=False),encoding='utf-8')
        git('add','--all');git('commit','--quiet','-m',message)
    (fixture/'.gitignore').write_text('.validation/\n',encoding='utf-8');commit('synthetic sources')
    fixture_build=search.build(fixture,node)
    fixture_hits=search.search(fixture,'regelcanaryeinfache',node)
    assert [x['path'] for x in fixture_hits['hits']]==['docs/Überblick.md']
    path.write_text('# Übersicht\nChanged synthetic source.\n',encoding='utf-8')
    stale_worker_calls=[]
    def forbidden_stale_worker(node,request):
        stale_worker_calls.append(request['action'])
        raise AssertionError('Stale source reached the QMD worker')
    try:search.search(fixture,'regelcanaryeinfache',node,worker=forbidden_stale_worker)
    except search.SearchError as exc:
        stale=exc.status
        assert stale=='stale' and not stale_worker_calls,(stale,stale_worker_calls)
    else:raise AssertionError('old hits accepted after edit')
    (fixture/'docs/empty.md').write_bytes(b'');manifest['search']['include'].append('docs/empty.md');commit('empty selected source')
    observed=[]
    def traced_worker(node,request):
        response=search.call_worker(node,request);observed.append(response);return response
    try:search.build(fixture,node,worker=traced_worker)
    except search.SearchError as exc:
        assert str(exc)=='QMD produced an incomplete index.',str(exc)
        partial={'status':exc.status,'message':str(exc)}
    else:raise AssertionError('QMD partial index accepted')
    assert observed[-1]['skipped']==0 and 'docs/empty.md' not in observed[-1]['paths']
    unready=search.status(fixture);assert unready['status']=='missing'
    synthetic={'unicode_source_found':True,'fixture_documents':fixture_build['documents'],'stale_after_source_edit':stale,'stale_worker_calls':len(stale_worker_calls),
        'partial_index_rejected':partial,'native_partial_report':observed[-1],'status_after_failed_build':unready}
report={'protocol':protocol,'protocol_sha256':sha((out/'protocol.json').read_bytes()),'build':built,'build_seconds':elapsed,
    'queries':results,'original_selected_bytes_unchanged':before==after,'synthetic_real_engine':synthetic,
    'claims':{'engine':'QMD 2.8.3, genuine native BM25','development_examples':True,'semantic_search':'NOT RUN','independent_retrieval_benchmark':False,'model_calls':0}}
(out/'result.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'report_directory':out.relative_to(root).as_posix(),'build':built,'positive_and_empty_queries':len(results),'original_bytes_unchanged':True,'synthetic':synthetic},ensure_ascii=False))
