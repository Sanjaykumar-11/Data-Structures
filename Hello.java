// import java.util.*;
// public class Hello {

//     public static void main(String[] args) {
//         Scanner input = new Scanner(System.in);
        
//         String s1 = input.next();
//         String s2 = input.next();
        
//         int row = s1.length();
//         int col = s2.length();
        
// 		int[][] matrix = new int[row][col];
		
		
// 		int max = 0;
		
// 		for(int i=0; i<row; i++)
// 		{
// 		    for(int j=0; j<col; j++)
// 		    {
// 		        if(s1.charAt(i)==s2.charAt(j))
// 		        {
// 		            if(i==0 || j==0)
// 		            {
// 		                matrix[i][j] = 1;
// 		            }
// 		            else
// 		            {
// 		                matrix[i][j] = 1 + matrix[i-1][j-1];
// 		            }
// 		        }
// 		        if(matrix[i][j]>max)
// 		        {
// 		            max = matrix[i][j];
// 		        }
// 		    }
// 		}
// 		System.out.println(max);
// 	}
// }







// import java.util.*;
// public class Hello {

//     public static void main(String[] args) {
//         Scanner input = new Scanner(System.in);
//         String s = input.nextLine();
//         int pos = 0;
//         int count = 0;
//         int maxlen = 0;
        
//         Map<Integer, Integer> map = new HashMap<>();
//         map.put(pos, count);
        
//         for(char ch: s.toCharArray())
//         {
//             pos++;
//             if(Character.isAlphabetic(ch))
//             {
//                 count++;
//             }
//             else
//             {
//                 count--;
//             }
//             if(map.containsKey(count))
//             {
//                 int current = pos-map.get(count);
//                 if(current>maxlen)
//                 {
//                     maxlen = current;
//                 }
//             }
//             else
//             {
//                 map.put(count, pos);
//             }
//         }
//         System.out.println(maxlen);

// 	}
// }





// import java.util.*;
// public class Hello {

//     public static void main(String[] args) {
// 		Scanner input = new Scanner(System.in);
// 		int M, N;
// 		M = input.nextInt();
// 		N = input.nextInt();
		
// 		int[] l = new int[10000];
// 		int[] arr = new int[10000];
		
// 		for(int i=0; i<M; i++)
// 		{
// 		    l[i] = input.nextInt();
// 		}
		
// 		for(int i=0; i<N; i++)
// 		{
// 		    arr[i] = input.nextInt();
// 		}
		
// 		int count = 0;
		
// 		for(int i=0; i<N; i++)
// 		{
// 		    for(int j=0; j<M; j++)
// 		    {
// 		        if(l[j]==arr[i])
// 		        {
//                     System.out.println("if entered");
// 		            count += 1;
// 		            break;
// 		        }
// 		    }
// 		}
		
// 		System.out.println(count);

// 	}
// }








// import java.util.*;
// public class Hello 
// {
//     public static void main(String[] args) 
//     {
// 		Scanner input = new Scanner(System.in);
// 		String s = input.nextLine();
// 		List<String> val = new ArrayList<>();
// 		for(int count=1; count<(1<<s.length()); count++)
// 		{
// 		    StringBuilder builder = new StringBuilder();
// 		    for(int i = 0; i<s.length(); i++)
// 		    {
// 		        if((count&(1<<i)) != 0)
// 		        {
// 		            builder.append(s.charAt(i));
// 		        }
// 		    }
// 		    val.add(builder.toString());
// 		}
//     	Collections.sort(val);
//     	for(String v:val)
//     	{
//     	    System.out.println(v);
//     	}
//     }
// }










// import java.util.*;
// public class Hello {
//     public static void main(String[] args) {
// 		Scanner input = new Scanner(System.in);
		
// 		int N = input.nextInt();
		
// 		int[] arr = new int[N];
// 	    for(int i=0; i<N; i++)
// 	    {
// 	        arr[i] = input.nextInt();
// 	    }
// 	    int ctr = 0;
// 	    for(int count=1; count<(1<<N); count++)
// 	    {
// 	        int sum=0;
// 	        for(int i=0; i<N; i++)
// 	        {
// 	            if((count&(1<<i))!=0)
// 	            {
// 	                sum+=arr[i];
// 	            }
// 	        }
// 	        if(sum==0)
// 	        {
// 	            ctr++;
// 	        }
// 	    }
// 	    System.out.println(ctr);
// 	}
// }






// STRING PERMUTATION

// import java.util.*;
// public class Hello 
// {
//     public void permute(char[] str, int left, int right)
//     {
//         if(left==right)
//         {
//             System.out.println(String.valueOf(str));
//             return;
//         }
//         for(int i = left; i <= right; i++)
//         {
//             char temp = str[left];
//             str[left] = str[i];
//             str[i] = temp;
//             //System.out.println("above");
//             permute(str, left+1, right);
//             //System.out.println("below");
//             temp = str[left];
//             str[left] = str[i];
//             str[i] = temp;
//         }
//     }
//     public static void main(String[] args) 
//     {
//         Hello per = new Hello();
        
// 		Scanner input = new Scanner(System.in);
		
// 		String s = input.nextLine();
		
// 		char[] str = s.toCharArray();
		
// 		per.permute(str, 0, str.length-1);

// 	}
// }






// Permutation Nearest Value

// import java.util.*;
// public class Hello {
//     public int nearest;
//     public int current;
    
//     public void permute(char[] str, int left, int right)
//     {
//         if(left==right)
//         {
//             int curr = Integer.parseInt(String.valueOf(str));
//             if(Math.abs(nearest - curr) < Math.abs(nearest - current))
//             {
//                // System.out.println(curr);
//                 this.current = curr;
//             }
//             return;
//         }
//         for(int i=left; i<=right; i++)
//         {
//             char temp = str[left];
//             str[left] = str[i];
//             str[i] = temp;
            
//             permute(str, left+1, right);
            
//             temp = str[left];
//             str[left] = str[i];
//             str[i] = temp;
//         }
//     }

//     public static void main(String[] args) {
// 		Scanner input = new Scanner(System.in);
// 		Hello per = new Hello();
		
// 		String s = input.next();
//         String n = input.next();

// 		per.nearest = Integer.valueOf(n);
		
// 		char[] str = s.toCharArray();
		
// 		per.permute(str, 0, str.length-1);

//         System.out.println(per.current);
// 	}
// }

// import java.util.*;
// class Slot
// {
//     int r;
//     int c;
// }

// public class Hello {
    
//     static int n = 9;
    
//     private static boolean solve(int[][] matrix)
//     {
//         Slot freeSlot = getFreeSlot(matrix);
//         if(freeSlot==null)
//         {
//             return true;
//         }
//         for(int digit=1; digit<=9; digit++)
//         {
//             if(canFillRow(matrix, freeSlot, digit) && canFillCol(matrix, freeSlot, digit) &&
//             canFillSubMatrix(matrix, freeSlot, digit))
//             {
//                 if(solve(matrix))
//                 {
//                     return true;
//                 }
//                 matrix[freeSlot.r][freeSlot.c]=0;
//             }
//         }
//         return false;
//     }
    
//     private static boolean canFillCol(int[][] matrix, Slot freeSlot, int digit)
//     {
//         for(int row=0; row<n; row++)
//         {
//             if(matrix[row][freeSlot.c]==digit)
//             {
//                 return false;
//             }
//         }
//         return true;
//     }
    
//     private static boolean canFillRow(int[][] matrix, Slot freeSlot, int digit)
//     {
//         for(int col=0; col<n; col++)
//         {
//             if(matrix[freeSlot.r][col] == digit)
//             {
//                 return false;
//             }
//         }
//         return true;
//     }
    
//     private static Slot getFreeSlot(int[][] matrix)
//     {
//         for(int i=0; i<n; i++)
//         {
//             for(int j=0; j<n; j++)
//             {
//                 if(matrix[i][j]==0)
//                 {
//                     Slot slot = new Slot();
//                     slot.r = i;
//                     slot.c = j;
//                     return slot;
//                 }
//             }
//         }
//         return null;
//     }
//     private static boolean canFillSubMatrix(int[][] matrix, Slot freeSlot, int digit)
//     {
//         int rowStart = (freeSlot.r/3)*3;
//         int colStart = (freeSlot.c/3)*3;
        
//         for(int row = rowStart; row<=rowStart+2; row++)
//         {
//             for(int col=colStart; col<=colStart+2; col++)
//             {
            
//                 if (matrix[row][col]==digit)
//                 {
//                     return false;
//                 }
//             }
//         }
//         return true;
//     }
    
    
    
    
//     public static void main(String[] args) {
// 		Scanner input = new Scanner(System.in);
// 		int matrix[][] = new int[n][n];
// 		for(int i=0; i<n; i++)
// 		{
// 		    for(int j=0; j<n; j++)
// 		    {
// 		        matrix[i][j] = input.nextInt();
// 		    }
// 		}
// 		if(solve(matrix))
// 		{
// 		    for(int i=0; i<n; i++)
// 		    {
// 		        for(int j=0; j<n; j++)
// 		        {
// 		            System.out.print(matrix[i][j]);
// 		        }
// 		    }
// 		    System.out.println();
// 		}
// 		else
// 		{
// 		    System.out.println("Not Solved");
// 		}
// 	}
// }

import java.util.*;
class Slot
{
    int r;
    int c;
}

public class Hello {
    
    static int n = 9;
    
    public static boolean solve(int[][] matrix)
    {
        Slot freeSlot = getFreeSlot(matrix);
        if(freeSlot==null)
        {
            return true;
        }
        for(int digit=1; digit<=9; digit++)
        {
            if(canFillRow(matrix, freeSlot, digit) && canFillCol(matrix, freeSlot, digit) &&
            canFillSubMatrix(matrix, freeSlot, digit))
            {
                matrix[freeSlot.r][freeSlot.c]=digit;
                if(solve(matrix))
                {
                    return true;
                }
                matrix[freeSlot.r][freeSlot.c]=0;
            }
        }
        return false;
    }
    
    public static boolean canFillCol(int[][] matrix, Slot freeSlot, int digit)
    {
        for(int row=0; row<n; row++)
        {
            if(matrix[row][freeSlot.c]==digit)
            {
                return false;
            }
        }
        return true;
    }
    
    public static boolean canFillRow(int[][] matrix, Slot freeSlot, int digit)
    {
        for(int col=0; col<n; col++)
        {
            if(matrix[freeSlot.r][col] == digit)
            {
                return false;
            }
        }
        return true;
    }
    
    public static Slot getFreeSlot(int[][] matrix)
    {
        for(int i=0; i<n; i++)
        {
            for(int j=0; j<n; j++)
            {
                if(matrix[i][j]==0)
                {
                    Slot slot = new Slot();
                    slot.r = i;
                    slot.c = j;
                    return slot;
                }
            }
        }
        return null;
    }


    public static boolean canFillSubMatrix(int[][] matrix, Slot freeSlot, int digit)
    {
        int rowStart = (freeSlot.r/3)*3;
        int colStart = (freeSlot.c/3)*3;
        
        for(int row = rowStart; row<=rowStart+2; row++)
        {
            for(int col=colStart; col<=colStart+2; col++)
            {
            
                if (matrix[row][col]==digit)
                {
                    return false;
                }
            }
        }
        return true;
    }
    
    
    
    
    public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		int matrix[][] = new int[n][n];
		for(int i=0; i<n; i++)
		{
		    for(int j=0; j<n; j++)
		    {
		        matrix[i][j] = input.nextInt();
		    }
		}
		if(solve(matrix))
		{
		    for(int i=0; i<n; i++)
		    {
		        for(int j=0; j<n; j++)
		        {
		            System.out.print(matrix[i][j]);
		        }
		    }
		    System.out.println();
		}
		else
		{
		    System.out.println("Not Solved");
		}
	}
}
    
    
    
    
//     public static void main(String[] args) {
// 		Scanner input = new Scanner(System.in);
// 		int matrix[][] = new int[n][n];
// 		for(int i=0; i<n; i++)
// 		{
// 		    for(int j=0; j<n; j++)
// 		    {
// 		        matrix[i][j] = input.nextInt();
// 		    }
// 		}
// 		if(solve(matrix))
// 		{
// 		    for(int i=0; i<n; i++)
// 		    {
// 		        for(int j=0; j<n; j++)
// 		        {
// 		            System.out.print(matrix[i][j]);
// 		        }
// 		    }
// 		    System.out.println();
// 		}
// 		else
// 		{
// 		    System.out.println("Not Solved");
// 		}
// 	}
// }


//Maximum sub matrix sum
// import java.util.*;
// public class Hello {

//     public static void main(String[] args) {
// 		Scanner input = new Scanner(System.in);
		
// 		int R = input.nextInt();
// 		int C = input.nextInt();
		
// 		int rowSum[][] = new int[R][C+1];
		
// 		for(int i=0; i<R; i++)
// 		{
// 		    for(int j=1; j<=C; j++)
// 		    {
// 		        int val = input.nextInt();
// 		        rowSum[i][j] = val + rowSum[i][j-1];
// 		    }
// 		}
// 		int K = input.nextInt();
// 		int maximumSum = 0;
// 		for(int i=0; i<=R-K; i++)
// 		{
// 		    for(int j=1; j<=C-K+1; j++)
// 		    {
// 		        int sum = 0;
// 		        for(int sumrow = i; sumrow<i+K; sumrow++)
// 		        {
// 		            sum += rowSum[sumrow][j+K-1] - rowSum[sumrow][j-1];
// 		        }
// 		        if(sum>maximumSum)
// 		        {
// 		            maximumSum = sum;
// 		        }
// 		    }
// 		}
// 		System.out.println(maximumSum);

// 	}
// }

//Minimum submatrix sum
// import java.util.*;
// public class Hello {

//     public static void main(String[] args) {
// 		Scanner input = new Scanner(System.in);
		
// 		int R = input.nextInt();
// 		int C = input.nextInt();
		
// 		int rowSum[][] = new int[R][C+1];
		
// 		for(int i=0; i<R; i++)
// 		{
// 		    for(int j=1; j<=C; j++)
// 		    {
// 		        int val = input.nextInt();
// 		        rowSum[i][j] = val + rowSum[i][j-1];
// 		    }
// 		}
		
// 		int K = input.nextInt();
// 		int minimumSum = Integer.MAX_VALUE;
// 		for(int i=0; i<=R-K; i++)
// 		{
// 		    for(int j=1; j<=C-K+1; j++)
// 		    {
// 		        int sum = 0;
// 		        for(int sumrow=i; sumrow<i+K; sumrow++)
// 		        {
// 		            sum += rowSum[sumrow][j+K-1]-rowSum[sumrow][j-1];
// 		        }
//                 if(sum<minimumSum)
//                 {
//                     minimumSum = sum;
//                 }
// 		    }
// 		}
//         System.out.println(minimumSum);
// 	}
// }