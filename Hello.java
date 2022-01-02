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