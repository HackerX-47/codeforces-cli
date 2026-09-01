from cfv2.imports import *
from cfv2.core.fetch_user import *
from cfv2.core.fetch_rating import *
from cfv2.core.fetch_submissions import *
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
    output_dir = Path(handle)
    output_dir.mkdir(parents=True, exist_ok=True)


    plt.figure()
    plt.plot(m_rating_change.index.astype(str), m_rating_change.values)
    plt.grid()
    plt.savefig(output_dir / "rating-trajectory.png")


    plt.figure()
    x_indexes = range(len(m_submissions))
    width = 0.2
    plt.bar([x - width for x in x_indexes] , m_submissions.values    , width = width, color="#444444")
    plt.bar([x for x in x_indexes]         , m_ac_submissions.values , width = width, color="#008fd5")
    plt.bar([x + width for x in x_indexes] , m_att_submissions       , width = width, color="#e5ae38")
    plt.xticks(
        list(x_indexes),
        m_submissions.index.astype(str)
    )
    plt.tight_layout()
    plt.savefig(output_dir / "monthly-solving.png")


    plt.figure()
    plt.barh(tag_count.index, tag_count.values)
    plt.tight_layout()
    plt.savefig(output_dir / "tag-performance.png")


    plt.figure()
    plt.bar(ac_rate_by_rating.index.astype(str), ac_rate_by_rating.values)
    plt.ylim(0, 100)
    plt.savefig(output_dir / "rating-range-performance.png")


    plt.figure()
    plt.bar(ac_rate_by_shift.index.astype(str), ac_rate_by_shift.values)
    plt.ylim(0, 100)
    plt.savefig(output_dir / "time-of-day-performance.png")


    plt.figure()
    plt.barh(verdict_count.index.astype(str), verdict_count.values)
    plt.savefig(output_dir / "verdict-count.png")