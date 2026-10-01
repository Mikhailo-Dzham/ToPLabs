import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
n = 1000





# Робимо вибірки
normal_sample = np.random.normal(0, 1, n)
cauchy_sample = np.random.standard_cauchy(n)

# Основна функція побудови
def create_boxplot_data(sample, method="quantile"):
    q1 = np.percentile(sample, 25)
    median = np.percentile(sample, 50)
    q3 = np.percentile(sample, 75)

    mean = np.mean(sample)
    std = np.std(sample, ddof=1)

    if method == "quantile":
        whisker_low = np.percentile(sample, 2.5)
        whisker_high = np.percentile(sample, 97.5)

    elif method == "std":
        # Вуса за формулою mean +/- 1.96 * std
        whisker_low = mean - 1.96 * std
        whisker_high = mean + 1.96 * std

    else:
        raise ValueError("Unknown method")

    return {
        "q1": q1,
        "median": median,
        "q3": q3,
        "whisker_low": whisker_low,
        "whisker_high": whisker_high,
        "mean": mean,
        "std": std
    }


# Отримання даних для графіків
normal_quantile = create_boxplot_data(
    normal_sample, "quantile"
)

normal_std = create_boxplot_data(
    normal_sample, "std"
)

cauchy_quantile = create_boxplot_data(
    cauchy_sample, "quantile"
)

cauchy_std = create_boxplot_data(
    cauchy_sample, "std"
)


# Функція побудови власного ящика
def draw_custom_boxplot(ax, data, title):

    box_data = [{
        "label": "",
        "q1": data["q1"],
        "med": data["median"],
        "q3": data["q3"],
        "whislo": data["whisker_low"],
        "whishi": data["whisker_high"],
        "fliers": []
    }]

    ax.bxp(
        box_data,
        showfliers=False,
        vert=False
    )

    ax.set_title(title)
    ax.grid(True, axis="x", alpha=0.3)


# Створення графіків
fig, axes = plt.subplots(2, 2, figsize=(14, 8))


# Нормальний розподіл
draw_custom_boxplot(
    axes[0, 0],
    normal_quantile,
    "Normal N(0,1) — Quantiles"
)

draw_custom_boxplot(
    axes[0, 1],
    normal_std,
    "Normal N(0,1) — Mean +/- 1.96*std"
)


# Розподіл Коші
draw_custom_boxplot(
    axes[1, 0],
    cauchy_quantile,
    "Cauchy C(0,1) — Quantiles"
)

draw_custom_boxplot(
    axes[1, 1],
    cauchy_std,
    "Cauchy C(0,1) — Mean +/- 1.96*std"
)


plt.tight_layout()
plt.show()


# Виведення статистики
def print_statistics(name, data):

    print(f"\n{name}")
    print(f"Q1: {data['q1']:.4f}")
    print(f"Median: {data['median']:.4f}")
    print(f"Q3: {data['q3']:.4f}")
    print(f"Mean: {data['mean']:.4f}")
    print(f"Std: {data['std']:.4f}")
    print(f"Whisker low: {data['whisker_low']:.4f}")
    print(f"Whisker high: {data['whisker_high']:.4f}")


print_statistics("Normal — Quantiles", normal_quantile)
print_statistics("Normal — Mean +/- 1.96*std", normal_std)

print_statistics("Cauchy — Quantiles", cauchy_quantile)
print_statistics("Cauchy — Mean +/- 1.96*std", cauchy_std)