import difflib
from pygments.lexers import get_lexer_by_name

def ponderar_similitudes(similitudes):

    n = len(similitudes)
    sum = 0

    for s in similitudes:
        sum += s
    
    print("Similitud ponderada: ", sum/n, "%")

def diferencia_por_tipo(cuentasA, cuentasB):

    if len(cuentasB) > len(cuentasA):
        tmp = cuentasA
        cuentasA = cuentasB
        cuentasB = tmp
    similitudes = [0] * len(cuentasA)

    for i, key in enumerate(cuentasA):
        if key in cuentasB:
            ma, mi = max(cuentasA[key], cuentasB[key]), min(cuentasA[key], cuentasB[key])
            similitudes[i] = (mi/ma)
            print("Similitud de ", key, " -> ", mi/ma * 100, "%")
        else:
            print("Hay tokens ", key, " en el mas grande pero no en el otro")
    
    ponderar_similitudes(similitudes)

print("=================High (java)=================")
codeA = ''
codeB = ''
with open('./clone_examples/high/A.java', 'r') as f:
    codeA = f.read()
with open('./clone_examples/high/B.java', 'r') as f:
    codeB = f.read()

lexer = get_lexer_by_name("java", stripall=True)
tokensA = lexer.get_tokens(codeA)
cuentaA = 0
tokensB = lexer.get_tokens(codeB)
cuentaB = 0

grouped_tokens_count_A = {}
for token in tokensA:
    count = grouped_tokens_count_A.get(str(token[0]), 0) + 1
    grouped_tokens_count_A[str(token[0])] = count
    cuentaA += 1

grouped_tokens_count_B = {}
for token in tokensB:
    count = grouped_tokens_count_B.get(str(token[0]), 0) + 1
    grouped_tokens_count_B[str(token[0])] = count
    cuentaB += 1

diferencia_por_tipo(grouped_tokens_count_A, grouped_tokens_count_B)

ma, mi = max(cuentaA, cuentaB), min(cuentaA, cuentaB)
print("similitud de conteo de tokens: ", (mi/ma)*100, "%")

tokensA = [token[1] for token in lexer.get_tokens(codeA)]
tokensB = [token[1] for token in lexer.get_tokens(codeB)]
matcher = difflib.SequenceMatcher(None, tokensA , tokensB)
print("Similarity simple: ", matcher.ratio())

print("=================  Mid (C)  =================")
with open('./clone_examples/med/A.c', 'r') as f:
    codeA = f.read()
with open('./clone_examples/med/B.c', 'r') as f:
    codeB = f.read()

lexer = get_lexer_by_name("java", stripall=True)
tokensA = lexer.get_tokens(codeA)
cuentaA = 0
tokensB = lexer.get_tokens(codeB)
cuentaB = 0

grouped_tokens_count_A = {}
for token in tokensA:
    count = grouped_tokens_count_A.get(str(token[0]), 0) + 1
    grouped_tokens_count_A[str(token[0])] = count
    cuentaA += 1

grouped_tokens_count_B = {}
for token in tokensB:
    count = grouped_tokens_count_B.get(str(token[0]), 0) + 1
    grouped_tokens_count_B[str(token[0])] = count
    cuentaB += 1

diferencia_por_tipo(grouped_tokens_count_A, grouped_tokens_count_B)

ma, mi = max(cuentaA, cuentaB), min(cuentaA, cuentaB)
print("similitud de conteo de tokens: ", (mi/ma)*100, "%")

tokensA = [token[1] for token in lexer.get_tokens(codeA)]
tokensB = [token[1] for token in lexer.get_tokens(codeB)]
matcher = difflib.SequenceMatcher(None, tokensA , tokensB)
print("Similarity simple: ", matcher.ratio())

print("=================Low (python)=================")

with open('./clone_examples/low/A.py', 'r') as f:
    codeA = f.read()
with open('./clone_examples/low/B.py', 'r') as f:
    codeB = f.read()

lexer = get_lexer_by_name("java", stripall=True)
tokensA = lexer.get_tokens(codeA)
cuentaA = 0
tokensB = lexer.get_tokens(codeB)
cuentaB = 0

grouped_tokens_count_A = {}
for token in tokensA:
    count = grouped_tokens_count_A.get(str(token[0]), 0) + 1
    grouped_tokens_count_A[str(token[0])] = count
    cuentaA += 1

grouped_tokens_count_B = {}
for token in tokensB:
    count = grouped_tokens_count_B.get(str(token[0]), 0) + 1
    grouped_tokens_count_B[str(token[0])] = count
    cuentaB += 1

diferencia_por_tipo(grouped_tokens_count_A, grouped_tokens_count_B)

ma, mi = max(cuentaA, cuentaB), min(cuentaA, cuentaB)
print("similitud de conteo de tokens: ", (mi/ma)*100, "%")

tokensA = [token[1] for token in lexer.get_tokens(codeA)]
tokensB = [token[1] for token in lexer.get_tokens(codeB)]
matcher = difflib.SequenceMatcher(None, tokensA , tokensB)
print("Similarity simple: ", matcher.ratio())