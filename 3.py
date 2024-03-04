Cho dãy số A[] có N phần tử là các số nguyên dương không quá 1000. Sau khi loại bỏ tất cả các giá trị bị lặp lại ở trong A[] ta tạo được dãy B[] có m phần tử là các giá trị khác nhau theo đúng thứ tự xuất hiện trong dãy A[].

Hãy tìm vị trí i nhỏ nhất (tính từ 0) trong dãy B[] thỏa mãn:

Tổng các phần tử từ B[0] đến B[i] là một số nguyên tố
Tổng các phần tử từ B[i+1] đến B[m-1] cũng là một số nguyên tố.
Input

Dòng đầu ghi số N (1 < N < 500).

Dòng tiếp theo ghi N số của dãy A[]

Output

Ghi ra vị trí i đầu tiên tìm được.

Nếu không có vị trí thỏa mãn thì ghi ra dòng chữ NOT FOUND