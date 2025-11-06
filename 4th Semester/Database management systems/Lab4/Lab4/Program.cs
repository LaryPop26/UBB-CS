using System;
using System.Data;
using System.Data.SqlClient;
using System.Threading;

namespace Deadlock
{
    internal class Program
    {
        private static string con = @"Server=LAR_LOQ\SQLEXPRESS;Database=VideoGamesStore;Integrated Security=True;TrustServerCertificate=True";

        static void Main(string[] args)
        {
            Thread thread1 = new Thread(T1);
            Thread thread2 = new Thread(T2);

            thread1.Start();
            thread2.Start();
        }

        static void T1()
        {
            Deadlock("P1"); // Stored procedure P1
        }

        static void T2()
        {
            Deadlock("P2"); // Stored procedure P2
        }

        static void Deadlock(string procName)
        {
            using (SqlConnection connection = new SqlConnection(con))
            {
                SqlCommand command = new SqlCommand(procName, connection)
                {
                    CommandType = CommandType.StoredProcedure
                };

                int tries = 3;
                while (tries > 0)
                {
                    try
                    {
                        connection.Open();
                        Console.WriteLine("Running stored procedure: " + procName);
                        command.ExecuteNonQuery();
                        Console.WriteLine(procName + " success");
                        break;
                    }
                    catch (SqlException ex)
                    {
                        Console.WriteLine(procName + " error: " + ex.Message);
                        if (ex.Number == 1205) // Deadlock
                        {
                            tries--;
                            Console.WriteLine("Retrying... Attempts left: " + tries);
                            Thread.Sleep(1000); // Optional: mică pauză înainte de retry
                        }
                        else
                        {
                            break;
                        }
                    }
                    finally
                    {
                        connection.Close();
                    }
                }

                if (tries == 0)
                {
                    Console.WriteLine(procName + " failed due to deadlock.");
                }
            }
        }
    }
}
