import matplotlib.pyplot as plt
import numpy as np

# Evidence-based baseline vs post-control outcomes.
# Values represent counts of verified conditions/control outcomes,
# not a percentage or security score.

categories = [
    "Critical vulnerabilities detected",
    "DB access restriction verified",
    "DB network isolation verified",
    "Governance controls implemented",
    "Baseline risks mitigated"
]

baseline = [1, 0, 0, 0, 0]
post_control = [0, 1, 1, 4, 3]

x = np.arange(len(categories))
width = 0.35

fig, ax = plt.subplots(figsize=(12, 7))

bars1 = ax.bar(
    x - width / 2,
    baseline,
    width,
    label="Baseline"
)

bars2 = ax.bar(
    x + width / 2,
    post_control,
    width,
    label="Post-control"
)

ax.set_title(
    "GRC102 Security Governance Control Outcomes",
    fontsize=16,
    fontweight="bold"
)

ax.set_xlabel(
    "Security governance outcome",
    fontsize=12
)

ax.set_ylabel(
    "Count of verified conditions / control outcomes",
    fontsize=12
)

ax.set_xticks(x)
ax.set_xticklabels(
    categories,
    rotation=25,
    ha="right"
)

ax.legend()

ax.grid(
    axis="y",
    linestyle="--",
    alpha=0.3
)

# Add values above each bar
for bars in [bars1, bars2]:
    for bar in bars:
        height = bar.get_height()
        ax.annotate(
            str(int(height)),
            xy=(bar.get_x() + bar.get_width() / 2, height),
            xytext=(0, 4),
            textcoords="offset points",
            ha="center",
            va="bottom",
            fontsize=10
        )

ax.set_ylim(0, 5)

plt.tight_layout()

plt.savefig(
    "control_outcomes_visualization.png",
    dpi=200,
    bbox_inches="tight"
)

plt.show()
