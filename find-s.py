mat = np.matrix(
"'s','w','n','s','w','s','yes';'s','w','h','s','w','s','yes';'r','c','h','s','w','c','no';'s','w','h','s','c','c','yes'"
print(mat[0][0])
num_att = 6
num_instance = 4
most_specific_hypothesis = ['O']*6
print(most_specific_hypothesis)
for i in range(num_instance):
if mat[i, -1] == 'yes':
for j in range(num_att):
if most_specific_hypothesis[j]=='O':
most_specific_hypothesis[j]=mat[i,j]
else:
if most_specific_hypothesis[j] != mat[i, j]:
most_specific_hypothesis[j] = '?'
else:
most_specific_hypothesis[j] = mat[i, j]
print(f"for instance no. {i} and {most_specific_hypothesis}")
