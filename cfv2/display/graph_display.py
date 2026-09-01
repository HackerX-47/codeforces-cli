from cfv2.imports import *

def graph_display(output_dir):

    print("\nGENERATING VISUAL REPORT")
    print("─" * 45)
    print(f"✓ Rating trajectory saved          → {output_dir / 'rating-trajectory.png'}")
    print(f"✓ Monthly solving activity saved   → {output_dir / 'monthly-solving.png'}")
    print(f"✓ Tag performance saved            → {output_dir / 'tag-performance.png'}")
    print(f"✓ Rating range performance saved   → {output_dir / 'rating-range-performance.png'}")
    print(f"✓ Time-of-day performance saved    → {output_dir / 'time-of-day-performance.png'}")
    print(f"✓ Verdict distribution saved       → {output_dir / 'verdict-count.png'}")