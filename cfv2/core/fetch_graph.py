from cfv2.imports import *
from cfv2.core.fetch_user import *
from cfv2.core.fetch_rating import *
from cfv2.core.fetch_submissions import *
from cfv2.display.graph_display import *
from pathlib import Path
import matplotlib.pyplot as plt

def fetch_graph(name):

    user_data = fetch_user_data(name, opt=0)
    rating_data = fetch_rating_data(name, opt=0)
    submission_data = fetch_submissions_data(
        name,
        last=100000,
        only_ac=False,
        lang=None,
        problem=None,
        opt=0
    )

    m_rating_change     = rating_data["m_rating_analysis"]["rating_end"]
    m_submissions       = pd.Series(submission_data["m_submissions"])
    m_ac_submissions    = pd.Series(submission_data["m_ac_submissions"])
    m_att_submissions   = pd.Series(submission_data["m_att_submissions"])
    tag_count           = pd.Series(submission_data["tag_count"])
    tag_count           = tag_count.iloc[::-1]
    ac_rate_by_rating   = pd.Series(submission_data["ac_rate_rating"])
    ac_rate_by_shift    = pd.Series(submission_data["ac_rate_shift"])   
    ac_rate_by_shift    = pd.concat([ac_rate_by_shift.iloc[1:], ac_rate_by_shift.iloc[:1]])
    verdict_count       = pd.Series(submission_data["verdict_count"])
    verdict_count       = verdict_count.iloc[::-1]

    handle = name
    output_dir = Path("images") / handle
    output_dir.mkdir(parents=True, exist_ok=True)

    # ======
    # 1
    # ======
    plt.figure(figsize=(10, 6))
    plt.style.use("dark_background")
    plt.plot(
        m_rating_change.index.astype(str),
        m_rating_change.values,
        color="#4F6D7A",
        marker="o",
        markersize=5,
        linewidth=2.5,
        markerfacecolor="#C49A5A",
        markeredgecolor="#4F6D7A"
    )

    plt.title("Rating Trajectory", fontsize=16, fontweight="bold")
    plt.style.use("dark_background")
    plt.xlabel("Month", fontsize=12)
    plt.ylabel("Rating", fontsize=12)

    plt.grid(axis="y", linestyle="--", alpha=0.4)
    plt.tight_layout()
    plt.savefig(output_dir / "rating-trajectory.png")
    plt.close()

    # ======
    # 2
    # ======
    plt.figure(figsize=(10,6))
    plt.style.use("dark_background")
    x_indexes = range(len(m_submissions))
    width = 0.2
    plt.bar(
        [x - width for x in x_indexes],
        m_submissions.values,
        width=width,
        color="#DCC9A9",
        label="Total Submissions"
    )

    plt.bar(
        [x for x in x_indexes],
        m_ac_submissions.values,
        width=width,
        color="#B83A2D",
        label="Accepted"
    )

    plt.bar(
        [x + width for x in x_indexes],
        m_att_submissions.values,
        width=width,
        color="#4E6851",
        label="Attempted"
    )
    
    plt.xticks(
        list(x_indexes),
        m_submissions.index.astype(str)
    )
    plt.title("Monthly Solving Activity", fontsize=16, fontweight="bold")
    plt.xlabel("Month", fontsize=12)
    plt.ylabel("Problem Solved", fontsize=12)

    plt.grid(axis="y", linestyle="--", alpha=0.4)
    plt.tight_layout()
    plt.savefig(output_dir / "monthly-solving.png")
    plt.close()

    # ======
    # 3
    # ======
    plt.figure(figsize=(10,6))
    plt.style.use("dark_background")
    plt.barh(
        tag_count.index,
        tag_count.values,
        color="#C05850",
        edgecolor="#C05850",
        linewidth=0.4
    )

    plt.title("Performance by Problem Tag")
    plt.xlabel("Acceptance Rate (%)")
    plt.ylabel("Problem Tag")

    plt.grid(axis="x", linestyle="--", alpha=0.4)
    plt.tight_layout()
    plt.savefig(output_dir / "tag-performance.png")
    plt.close()

    # ======
    # 4
    # ======
    plt.figure(figsize=(10,6))
    plt.style.use("dark_background")
    plt.bar(
        ac_rate_by_rating.index.astype(str),
        ac_rate_by_rating.values,
        color="#BC96E6",
        linewidth=0.4
    )

    plt.title("Performance by Problem Rating")
    plt.xlabel("Problem Rating")
    plt.ylabel("Acceptance Rate (%)")

    plt.ylim(0, 100)
    plt.grid(axis="y", linestyle="--", alpha=0.4)
    plt.tight_layout()
    plt.savefig(output_dir / "rating-range-performance.png")
    plt.close()

    # ======
    # 5
    # ======
    plt.figure(figsize=(10,6))
    plt.style.use("dark_background")
    plt.bar(
        ac_rate_by_shift.index.astype(str),
        ac_rate_by_shift.values,
        color="#FBE4D8",
        edgecolor="#FBE4D8",
        linewidth=0.4
    )

    plt.title("Performance by Time of Day")
    plt.xlabel("Time of Day")
    plt.ylabel("Acceptance Rate (%)")

    plt.ylim(0, 100)
    plt.grid(axis="y", linestyle="--", alpha=0.4)
    plt.tight_layout()
    plt.savefig(output_dir / "time-of-day-performance.png")
    plt.close()

    # ======
    # 6
    # ======
    plt.figure(figsize=(10,6))
    plt.style.use("dark_background")
    plt.barh(
        verdict_count.index.astype(str),
        verdict_count.values,
        color="#9792CB",
        edgecolor="#9792CB",
        linewidth=0.4
    )

    plt.title("Submission Verdict Distribution")
    plt.xlabel("Verdict")
    plt.ylabel("Number of Submissions")

    plt.grid(axis="x", linestyle="--", alpha=0.4)
    plt.tight_layout()
    plt.savefig(output_dir / "verdict-count.png")
    plt.close()


    graph_display(output_dir)