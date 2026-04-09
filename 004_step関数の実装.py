"""
- 003を関数化
"""

def f(x):
    return x ** 2

def grad(x):
    return 2 * x # 勾配計算

def step(x, lr, grad):
    return x - lr * grad # パラメータを更新

lr = 0.1
x = 3 # 変数の初期値。この値を更新する
for i in range(1, 11):
    g = grad(x)
    x = step(x, lr, g)
    print(f"現在のステップ{i} | 現在の変数 x={x:.3f} | 現在の関数値:y={f(x)}") # 今回の変数を出力
