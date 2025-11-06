import java.util.Arrays;
import java.util.Random;

public class Main {

    private static final int P = 16;
    private static final int N = 1000000;
    private static final int MAX_VAL = 14500;
    private static int[] a = new int[N];
    private static int[] b = new int[N];
    private static int[] c = new int[N];
    private static int[] c_secv = new int[N];

    private static final Random rnd = new Random();

    private static void init(int[] v) {
        for (int i = 0; i < v.length; i++) {
            v[i] = rnd.nextInt(MAX_VAL);
        }
    }

    private static void print_arr(int[] v, int no_elems) {
        for (int i = 0; i < v.length && i< no_elems; i++) {
            System.out.printf("%6d ", v[i]);
        }
        System.out.println();
    }

    private static void sum(int[] a, int[] b, int[] c) {
        assert a.length == b.length && a.length == c.length;

        for (int i = 0; i < a.length; i++) {
//            c[i] = a[i] + b[i];
            c[i] = (int)Math.pow(a[i],3.0/2.0)+ (int) Math.pow(b[i],2.0/3.0);
        }
    }

    public static void main(String[] args) {
        init(a);
        init(b);

        long start_time_secv = System.nanoTime();
        sum(a, b, c_secv);
        long end_time_secv = System.nanoTime();

        MyThread[] threads = new MyThread[P];

        long start_time_par = System.nanoTime();

        int dim_data = N / P;
        int r = N % P;
        int start_idx = 0;
        int end_idx = dim_data;

        for (int tid = 0; tid < P; tid++) {
            if (r>0) {
                end_idx += 1;
                r-=1;
            }

            threads[tid] = new MyThread(a,b,c,start_idx,end_idx);
            threads[tid].start();

            start_idx = end_idx;
            end_idx += dim_data;
        }

        try {
            for (MyThread t : threads) {
                t.join();
            }
        } catch (InterruptedException ex) {
            ex.printStackTrace();
        }

        long end_time_par = System.nanoTime();
        if (Arrays.equals(c, c_secv)) {
            System.out.println("All good!");
        } else {
            System.out.println("Mismatch!");
        }

        print_arr(a, 5);
        print_arr(b, 5);
        print_arr(c, 5);
        print_arr(c_secv, 5);

        long secv_delta = end_time_secv - start_time_secv;
        long par_delta = end_time_par - start_time_par;

        double secv_delta_us = secv_delta / 1e3;
        double par_delta_us = par_delta / 1000f;
        System.out.printf("Secv time: %10.3fus\n", secv_delta_us);
        System.out.printf("Par time: %10.3fus\n", par_delta_us);
    }
}