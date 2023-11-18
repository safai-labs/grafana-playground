#!/usr/bin/python3


import csv
import random
from datetime import datetime
import argparse

# Define the kinds of files
KINDS = [
    "ArbitraryBinaryData",
    "Application",
    "Archive",
    "Audio",
    "Book",
    # ... add other kinds here as needed ...
    "VirtualMachine",
]


def generate_entry(uid, kind):
    """Generate a random entry for a given user and kind of file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    total_creates = random.randint(0, 10)
    total_reads = random.randint(0, 10)
    total_writes = random.randint(0, 10)
    total_deletes = random.randint(0, 10)
    bytes_created = random.randint(0, 5000)
    bytes_read = random.randint(0, 5000)
    bytes_written = random.randint(0, 5000)
    bytes_deleted = random.randint(0, 5000)

    return [
        timestamp,
        uid,
        kind,
        total_creates,
        total_reads,
        total_writes,
        total_deletes,
        bytes_created,
        bytes_read,
        bytes_written,
        bytes_deleted,
    ]


def simulate_ransomware_attack(uid):
    """Generate a ransomware-like activity entry for a given user."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Targeted file types for reading and encrypting.
    target_kinds = ["Document", "Image", "Video", "SourceCode", "Database"]
    kind = random.choice(target_kinds)

    # Significant spike in read operations as ransomware scans and reads files.
    total_reads = random.randint(100, 200)

    # Encrypted files get written, either replacing the originals or as new files.
    total_writes = random.randint(100, 200)

    # Deletion of original files post-encryption.
    total_deletes = random.randint(100, 200)

    # Creation of encrypted files or ransom notes.
    if kind == "ArbitraryBinaryData":
        total_creates = random.randint(150, 250)
    else:
        total_creates = random.randint(50, 100)

    # Data sizes would be larger due to file encryption.
    bytes_created = random.randint(50000, 100000)
    bytes_read = random.randint(50000, 100000)
    bytes_written = random.randint(50000, 100000)
    bytes_deleted = random.randint(50000, 100000)

    return [
        timestamp,
        uid,
        kind,
        total_creates,
        total_reads,
        total_writes,
        total_deletes,
        bytes_created,
        bytes_read,
        bytes_written,
        bytes_deleted,
    ]


def generate_csv_file(n_users, m_kinds, filename="telemetry_data.csv"):
    """Generate a CSV file with random activity entries for N users and M kinds of files."""
    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(
            [
                "Timestamp",
                "UID",
                "Kind",
                "TotalCreates",
                "TotalReads",
                "TotalWrites",
                "TotalDeletes",
                "BytesCreated",
                "BytesRead",
                "BytesWritten",
                "BytesDeleted",
            ]
        )

        for uid in range(1, n_users + 1):
            for _ in range(m_kinds):
                kind = random.choice(KINDS)
                entry = generate_entry(uid, kind)
                writer.writerow(entry)


def main():
    parser = argparse.ArgumentParser(
        description="Generate a CSV file with random activity entries for N users and M kinds of files."
    )
    parser.add_argument(
        "-u", "--users", type=int, required=True, help="Number of users (N)"
    )
    parser.add_argument(
        "-k", "--kinds", type=int, required=True, help="Number of file kinds (M)"
    )
    parser.add_argument(
        "-f",
        "--filename",
        type=str,
        default="telemetry_data.csv",
        help="Output CSV filename (default: telemetry_data.csv)",
    )
    parser.add_argument(
        "-r", "--ransomware", action="store_true", help="Simulate ransomware attack"
    )

    args = parser.parse_args()

    # Generate a list of random UIDs
    user_ids = [random.randint(1000, 9999) for _ in range(args.users)]

    # If ransomware flag is present, choose a "bad uid"
    bad_uid = random.choice(user_ids) if args.ransomware else None

    with open(args.filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(
            [
                "Timestamp",
                "UID",
                "Kind",
                "TotalCreates",
                "TotalReads",
                "TotalWrites",
                "TotalDeletes",
                "BytesCreated",
                "BytesRead",
                "BytesWritten",
                "BytesDeleted",
            ]
        )

        for uid in user_ids:
            for _ in range(args.kinds):
                if uid == bad_uid:
                    entry = simulate_ransomware_attack(uid)
                else:
                    kind = random.choice(KINDS)
                    entry = generate_entry(uid, kind)
                writer.writerow(entry)
    print(
        f"Generated {args.filename} with random activity entries for {args.users} users and {args.kinds} kinds of files."
    )


if __name__ == "__main__":
    main()
