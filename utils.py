def function(x):
	if x%2 is 0:
		return x+1
	return x-5
	
def function2(x):
	if x%3 is 0:
		return x-3
	return x-7

def swap(ai,aj,bi,bj, image, arr):
	# Code to swap pixel RGB values
	arr[ai,aj],arr[bi,bj]= arr[bi,bj],arr[ai,aj]

def efficiency(orig, enco, W, H):
	different = 0
	for i in range(W):
		for j in range(H):
			if orig[i,j]!=enco[i,j]:
				different = different+1
	print('Different pixels: '+ str(different))
	print('Total pixels: '+ str(W*H))
	print('Efficiency: '+ str(different*100.0/(W*H)) +" %")

def cascade(xy, N, W, H):
	cas= []
	cas.append((xy[0]%W,xy[1]%H))
	i= 0
	for i in range(N):
		xy= (function(xy[0])%W,function(xy[1])%H)
		cas.append(xy)
	return cas


def automate_swap(alpha, beta, N, image, arr):
	for i in range(N):
		swap(alpha[i][0],alpha[i][1],beta[i][0],beta[i][1], image, arr)

def automate_swap_dec(alpha, beta, N, image, arr):
	for i in range(N):
		swap(alpha[N-1-i][0],alpha[N-1-i][1],beta[N-1-i][0],beta[N-1-i][1], image, arr)

