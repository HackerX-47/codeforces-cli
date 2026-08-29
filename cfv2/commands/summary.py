from cfv2.imports import *
from cfv2.core.fetch_user import *
from cfv2.core.fetch_rating import *
from cfv2.core.fetch_submissions import *
from cfv2.gemini import ask_gemini
from cfv2.display.gemini_display import *

@click.command()
@click.argument("name")
def summary(name):

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

    prompt = f"""
    You are a Codeforces performance analyst.

    Analyze the following Codeforces user's complete performance data.

    IMPORTANT RULES:
    - Use only the data provided below.
    - Do not invent statistics or facts.
    - Do not assume missing information.
    - Identify meaningful trends and weaknesses.
    - Distinguish between attempts and successfully solved problems.
    - When discussing acceptance rate, consider the number of submissions as context.
    - Give actionable advice based on the evidence.
    - Keep the analysis concise but insightful.

    ================ USER PROFILE ================

    {user_data}

    ================ RATING PERFORMANCE ================

    Total contests:             {rating_data["totalContest"]}
    Current rating:             {rating_data["currRating"]}
    Best rating:                {rating_data["bestRating"]}
    Worst rating:               {rating_data["worstRating"]}
    Best contest rank:          {rating_data["bestRank"]}
    Worst contest rank:         {rating_data["worstRank"]}
    Average contest rank:       {rating_data["avgRank"]}
    Average rating change per contest: {rating_data["avgRatingChng"]}
    Positive rating changes:    {rating_data["posChngCount"]}
    Negative rating changes:    {rating_data["negChngCount"]}
    No rating change:           {rating_data["noChngCount"]}
    Overall rating change:      {rating_data["ovlRatingChng"]}

    Monthly rating progression:
    {rating_data["m_rating_analysis"].to_dict(orient="index")}

    ================ SUBMISSION PERFORMANCE ================

    Total submissions: {submission_data["count"]}

    Verdict counts:             {submission_data["verdict_count"]}
    Most used language:         {submission_data["lang"]}
    Unique problems attempted:  {submission_data["unique_attempt"]}
    Unique problems solved:     {submission_data["unique_ac"]}

    Average attempts required to solve a problem:    
                                {submission_data["avg_attempts"]}

    ================ PROBLEM DIFFICULTY ================

    Problems attempted by rating:
    {submission_data["attempt_rating"]}

    Problems solved by rating:
    {submission_data["solved_rating"]}

    Average solved problem rating:
    {submission_data["avg_sol_rating"]}

    Highest solved problem rating:
    {submission_data["hi_sol_rating"]}

    Lowest solved problem rating:
    {submission_data["lo_sol_rating"]}

    Acceptance rate by problem rating:
    {submission_data["ac_rate_rating"]}

    ================ TAG PERFORMANCE ================

    Problem tag counts:
    {submission_data["tag_count"]}

    ================ TIME OF DAY ================

    Submissions by shift:
    {submission_data["shift_count"]}

    Accepted submissions by shift:
    {submission_data["ac_shift_count"]}

    Acceptance rate by shift:
    {submission_data["ac_rate_shift"]}

    ================ MONTHLY PROGRESS ================

    Monthly total submissions:
    {submission_data["m_submissions"]}

    Monthly unique solved problems:
    {submission_data["m_ac_submissions"]}

    Monthly unique attempted problems:
    {submission_data["m_att_submissions"]}

    Monthly acceptance rate:
    {submission_data["m_ac_rate"]}

    Monthly average attempts to solve:
    {submission_data["m_avg_attempts"]}

    Monthly average solved problem rating:
    {submission_data["m_avg_rating_sol"]}

    ================ REQUIRED ANALYSIS ================

    Give the user a personal Codeforces performance report with these sections:

    1. OVERALL PERFORMANCE
    - Current level and general performance.
    - Strongest measurable aspects.
    - Biggest weaknesses.

    2. RATING JOURNEY
    - Explain the rating progression.
    - Identify whether the user is improving, stagnating, or declining.
    - Mention significant changes visible in the monthly progression.

    3. PROBLEM DIFFICULTY
    - Identify the rating range the user appears most comfortable solving.
    - Compare attempted vs solved difficulty.
    - Comment on the highest-rated problems solved.

    4. TAG PERFORMANCE
    - Identify the user's strongest and weakest areas based on the available tag data.
    - Do not call a tag "weak" merely because it has a low solve count; consider the available data carefully.

    5. TIME-OF-DAY PERFORMANCE
    - Identify the strongest shift based on acceptance rate.
    - Consider submission volume before making a strong conclusion.
    - Mention if the sample size is too small to make a reliable conclusion.

    6. MONTHLY PROGRESSION
    - Explain whether solving volume is increasing or decreasing.
    - Explain whether problem difficulty is increasing.
    - Explain whether efficiency/acceptance is improving.
    - Identify notable changes over time.

    7. ACTION PLAN
    - Give 3-5 concrete recommendations for improving on Codeforces.
    - Base every recommendation on the supplied data.

    Use concrete numbers from the data where useful.
    Do not simply repeat the raw statistics; interpret them.



    ================ OUTPUT FORMAT ================

    The response will be displayed directly in a terminal CLI.
    DO NOT use Markdown formatting.

    STRICTLY DO NOT use:

    * `#`, `##`, `###` headings
    * `**bold**`
    * `*italic*`
    * Markdown tables
    * Markdown links
    * Code fences

    Instead, use plain-text terminal formatting.

    Use this hierarchy:

    MAIN TITLE

    [1] SECTION NAME

    Subsection Name
    • Point
    • Point

    For important metrics, use this format:

    Rating        : 985
    Problems      : 247
    Acceptance    : 52.63%

    For analysis, use short paragraphs underneath the relevant
    subsection.

    Use:

    * UPPERCASE for the main report title.
    * `[1]`, `[2]`, `[3]` etc. for major sections.
    * A line of `-` characters below major section headings.
    * Indentation using two spaces for details.
    * `•` for bullet points.
    * `:` to separate metric names and values.
    * Blank lines between major sections.

    Keep the hierarchy visually consistent throughout the report.

    Do not print raw dictionaries, Python objects, DataFrames, or
    JSON unless absolutely necessary. Convert the information into
    human-readable statements.

    ================ REPORT STRUCTURE ================

    Create the report using exactly these major sections:

    [1] OVERALL PERFORMANCE
    [2] RATING JOURNEY
    [3] PROBLEM DIFFICULTY
    [4] TAG PERFORMANCE
    [5] TIME-OF-DAY PERFORMANCE
    [6] MONTHLY PROGRESSION
    [7] ACTION PLAN

    For each section:

    * Give the important numerical evidence.
    * Explain what the numbers mean.
    * Focus on trends rather than simply repeating statistics.
    * Do not make claims that are unsupported by the provided data.

    ================ ANALYSIS STYLE ================

    Act as a Codeforces performance analyst.

    The goal is to help the user understand their actual
    competitive-programming progress.

    Be:

    * Analytical
    * Specific
    * Honest
    * Concise
    * Action-oriented

    When identifying a weakness, support it with data.

    When identifying a strength, support it with data.

    Do not exaggerate small differences.

    If the sample size is too small to draw a reliable conclusion,
    explicitly say so.

    Do not invent missing data.

    Do not assume that correlation means causation.

    Use concrete numbers when they strengthen the analysis.

    ================ ACTION PLAN ================

    End with 3-5 concrete recommendations.

    Every recommendation must contain:

    Recommendation
    What the user should do.

    Evidence
    The specific metric or trend supporting the recommendation.

    Why
    Why this change could improve their performance.

    Prioritize recommendations by importance.

    ================ FINAL INSTRUCTION ================

    Return ONLY the finished Codeforces performance report.

    Do not include an introduction such as:
    "Here is your personalized report."

    Do not include a closing message.

    Make the report clean and readable when printed directly
    in a Linux terminal.

    One more thing: Format text to fit within the terminal width of 150 chars. Prefer wrapping at word boundaries and never split a word unless absolutely necessary.

    Format every recommendation using this exact terminal-friendly structure:

    [04] STABILIZE CONTEST PERFORMANCE
    ──────────────────────────────────

    INSIGHT
    Rating fell 4009 → 3528 (-481).

    RECENT DAMAGE
    Apr 2026  -282
    Aug 2025  -201

    ACTION
    Prioritize consistent contest execution.
    Goal: stabilize rating and recover toward 4000.

    RULES:

    * Keep the output clean, compact, and terminal-friendly.
    * Use uppercase section labels: INSIGHT, EVIDENCE, RECENT DAMAGE, ACTION, WHY, etc.
    * Put the recommendation title on the first line.
    * Use a horizontal separator below the title.
    * Keep each line within the available terminal width.
    * NEVER break or split words.
    * Wrap long sentences at word boundaries.
    * Prefer short, information-dense sentences.
    * Use 1–2 lines maximum for INSIGHT and ACTION explanations.
    * Use bullets only when listing multiple pieces of evidence.
    * Put important numbers, rating changes, dates, and metrics on separate lines when useful.
    * Do not use Markdown headings such as #, ##, or ###.
    * Do not use tables.
    * Do not use long paragraphs.
    * Do not add unnecessary introductory or concluding text.
    * Maintain consistent spacing between sections.
    * Recommendation numbers must use two digits: [01], [02], [03], etc.
    * The final output should look natural in a Unix/Linux terminal.

    If the terminal width is unknown, assume a safe content width of 150 characters.

    """

    output_print(ask_gemini(prompt))
