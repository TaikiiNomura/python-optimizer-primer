"""
- 変数の更新の履歴を保存する
"""

def f(x):
    return x ** 2

def grad(x):
    return 2 * x # 勾配計算

def step(x, lr, grad):
    return x - lr * grad # パラメータを更新

lr = 0.1
x = 3 # 変数の初期値。この値を更新する

results = [] # ここに履歴を保存
for i in range(1, 11):
    g = grad(x)
    x = step(x, lr, g)
    print(f"現在のステップ{i} | 現在の変数 x={x:.3f} | 現在の関数値:y={f(x)}") # 今回の変数を出力
    results.append(x)

# print(results) # 履歴を確認
# 結果をグラフに表示する

import matplotlib.pyplot as plt

steps = list(range(1, len(results) + 1))

plt.plot(steps, results)
plt.xlabel("Step")
plt.ylabel("x")
plt.title("x history")
plt.show()

import numpy as np

x_vals = np.linspace(-5, 5, 100)
y_vals = f(x_vals)

plt.plot(x_vals, y_vals)

y_history = [f(x) for x in results]
plt.scatter(results, y_history)

plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("x^2 history")
plt.show()
