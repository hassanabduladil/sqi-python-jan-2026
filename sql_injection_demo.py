"""
SQL Injection Demo — Educational Purpose
==========================================
This script demonstrates:
  1. HOW a SQL injection attack works (vulnerable code)
  2. HOW to prevent it (parameterized queries)

Run it and follow the prompts!
"""

import sqlite3
import os

DB_NAME = "demo_school.db"


# ── Setup: create a small demo database ──────────────────────────────
def setup_database():
    if os.path.exists(DB_NAME):
        os.remove(DB_NAME)

    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE students (
            id    INTEGER PRIMARY KEY,
            name  TEXT NOT NULL,
            grade TEXT NOT NULL,
            gpa   REAL NOT NULL
        )
    """)

    cur.execute("""
        CREATE TABLE secret_admin (
            id       INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    """)

    students = [
        (1, "Alice Johnson",  "A",  3.9),
        (2, "Bob Smith",      "B+", 3.4),
        (3, "Carol Williams", "A-", 3.7),
        (4, "David Brown",    "B",  3.1),
        (5, "Eve Davis",      "A+", 4.0),
    ]
    cur.executemany("INSERT INTO students VALUES (?, ?, ?, ?)", students)

    # A "secret" table the attacker shouldn't be able to see
    cur.execute("INSERT INTO secret_admin VALUES (1, 'admin', 'supersecret123')")

    conn.commit()
    return conn


# ── VULNERABLE version (string concatenation) ────────────────────────
def search_vulnerable(conn, user_input):
    """
    ⚠️  BAD PRACTICE — builds SQL by concatenating user input directly.
    This is exactly how SQL injection happens.
    """
    query = "SELECT * FROM students WHERE name = '" + user_input + "'"
    print(f"\n  [DEBUG] Query sent to DB:\n    {query}")

    cur = conn.cursor()
    try:
        # executescript can run multiple statements — worst case scenario
        # We use execute here; the injection still works via UNION, OR, etc.
        results = cur.execute(query).fetchall()
        return results
    except Exception as e:
        return f"SQL Error: {e}"


# ── SAFE version (parameterized query) ───────────────────────────────
def search_safe(conn, user_input):
    """
    ✅  BEST PRACTICE — uses a parameterized query (placeholder ?).
    The database driver treats the input as DATA, never as SQL code.
    """
    query = "SELECT * FROM students WHERE name = ?"
    print(f"\n  [DEBUG] Query template:\n    {query}")
    print(f"  [DEBUG] Parameter value:\n    {user_input!r}")

    cur = conn.cursor()
    try:
        results = cur.execute(query, (user_input,)).fetchall()
        return results
    except Exception as e:
        return f"SQL Error: {e}"


# ── Interactive demo ─────────────────────────────────────────────────
def print_results(results):
    if isinstance(results, str):
        print(f"  ❌ {results}")
    elif not results:
        print("  (no rows returned)")
    else:
        for row in results:
            print(f"  → {row}")


def run_demo():
    conn = setup_database()
    separator = "=" * 60

    print(separator)
    print("  SQL INJECTION DEMO — for educational purposes only")
    print(separator)

    # ── Demo 1: Normal lookup ─────────────────────────────────────
    print("\n📘 DEMO 1 — Normal search (nothing malicious)")
    print("-" * 50)
    normal_input = "Alice Johnson"
    print(f"  User types: {normal_input}")

    print("\n  ⚠️  Vulnerable function:")
    print_results(search_vulnerable(conn, normal_input))

    print("\n  ✅ Safe function:")
    print_results(search_safe(conn, normal_input))

    # ── Demo 2: Tautology attack (OR 1=1) ─────────────────────────
    print(f"\n\n📘 DEMO 2 — Tautology attack: retrieve ALL rows")
    print("-" * 50)
    attack_input = "' OR '1'='1"
    print(f"  User types: {attack_input}")

    print("\n  ⚠️  Vulnerable function (leaks every student!):")
    print_results(search_vulnerable(conn, attack_input))

    print("\n  ✅ Safe function (treats it as a literal name → no match):")
    print_results(search_safe(conn, attack_input))

    # ── Demo 3: UNION attack (read another table!) ────────────────
    print(f"\n\n📘 DEMO 3 — UNION attack: read the secret_admin table")
    print("-" * 50)
    union_input = "' UNION SELECT id, username, password, 0 FROM secret_admin --"
    print(f"  User types: {union_input}")

    print("\n  ⚠️  Vulnerable function (exposes admin credentials!):")
    print_results(search_vulnerable(conn, union_input))

    print("\n  ✅ Safe function (harmless — no match):")
    print_results(search_safe(conn, union_input))

    # ── Demo 4: Interactive playground ────────────────────────────
    print(f"\n\n{'=' * 60}")
    print("  🎮 INTERACTIVE MODE — try your own inputs!")
    print("     Type 'quit' to exit.")
    print(f"{'=' * 60}")

    while True:
        user = input("\n  Enter a search term: ").strip()
        if user.lower() == "quit":
            break
        print("\n  ⚠️  Vulnerable:")
        print_results(search_vulnerable(conn, user))
        print("\n  ✅ Safe:")
        print_results(search_safe(conn, user))

    conn.close()
    if os.path.exists(DB_NAME):
        os.remove(DB_NAME)
    print("\n  👋 Demo complete. Stay safe out there!\n")


# ── Summary slide ────────────────────────────────────────────────────
def print_summary():
    print("""
╔══════════════════════════════════════════════════════════════╗
║                   KEY TAKEAWAYS                             ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  ❌ NEVER do this:                                           ║
║     query = "SELECT * FROM t WHERE x='" + user_input + "'"  ║
║     cursor.execute(query)                                    ║
║                                                              ║
║  ✅ ALWAYS do this:                                          ║
║     query = "SELECT * FROM t WHERE x = ?"                    ║
║     cursor.execute(query, (user_input,))                     ║
║                                                              ║
║  Why it works:                                               ║
║   • The DB driver escapes/binds the parameter as DATA        ║
║   • The input can NEVER be interpreted as SQL code           ║
║   • Works the same in every language (?, %s, :name, @p1)     ║
║                                                              ║
║  Extra defenses (defense in depth):                          ║
║   • Validate / sanitize input on the application side        ║
║   • Use an ORM (SQLAlchemy, Django ORM, etc.)                ║
║   • Apply least-privilege DB permissions                     ║
║   • Never expose raw DB errors to end users                  ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
""")


if __name__ == "__main__":
    print_summary()
    run_demo()