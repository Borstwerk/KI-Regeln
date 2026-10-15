using System;

internal static class Program
{
    private static decimal Discount(decimal price, decimal rate)
    {
        if (price < 0m || rate < 0m || rate > 1m)
            throw new ArgumentOutOfRangeException(nameof(rate));
        return Math.Round(price * (1m - rate), 2, MidpointRounding.AwayFromZero);
    }

    private static void Expect(decimal expected, decimal actual, string name)
    {
        if (expected != actual)
            throw new InvalidOperationException($"{name}: expected {expected}, observed {actual}");
    }

    private static int Main()
    {
        try
        {
            Expect(80m, Discount(100m, 0.2m), "ordinary discount");
            Expect(0m, Discount(0m, 0.2m), "zero");
            Expect(10m, Discount(19.99m, 0.5m), "rounding");
            Expect(0m, Discount(125m, 1m), "full discount");
            try
            {
                Discount(1m, 1.2m);
                throw new InvalidOperationException("Invalid rate was not rejected.");
            }
            catch (ArgumentOutOfRangeException) { }
            Console.WriteLine("NATIVE_DOTNET_ASSERTIONS_PASS");
            return 0;
        }
        catch (Exception ex)
        {
            Console.Error.WriteLine("Native checks failed: " + ex.GetType().Name);
            return 1;
        }
    }
}
