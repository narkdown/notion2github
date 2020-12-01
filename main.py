import os
import json
import argparse
from narkdown.exporter import NotionExporter


def str2bool(v):
    if isinstance(v, bool):
        return v
    if v.lower() in ("yes", "true", "t", "y", "1"):
        return True
    elif v.lower() in ("no", "false", "f", "n", "0"):
        return False
    else:
        raise argparse.ArgumentTypeError("Boolean value expected.")


def str2dict(s):
    return json.loads(s.replace("'", '"'))


def parse_args():
    parser = argparse.ArgumentParser(
        description="Export markdown docs from notion database."
    )
    parser.add_argument("database_url")
    parser.add_argument("--docs-directory", default="./docs")
    parser.add_argument("--recursive-export", type=str2bool, default=True)
    parser.add_argument("--create-page-directory", type=str2bool, default=True)
    parser.add_argument("--add-metadata", type=str2bool, default=False)
    parser.add_argument("--lower-pathname", type=str2bool, default=False)
    parser.add_argument("--lower-filename", type=str2bool, default=False)
    parser.add_argument("--line-break", type=str2bool, default=False)
    parser.add_argument("--category-column-name", default="")
    parser.add_argument("--tags-column-name", default="")
    parser.add_argument("--created-time-column-name", default="")
    parser.add_argument("--status-column-name", default="")
    parser.add_argument("--current-status", default="")
    parser.add_argument("--next-status", default="")
    parser.add_argument("--filters", default="{}")

    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()

    token = os.environ.get("NOTION_TOKEN")
    args.filters = str2dict(args.filters)

    NotionExporter(
        token,
        docs_directory=args.docs_directory,
        recursive_export=args.recursive_export,
        create_page_directory=args.create_page_directory,
        add_metadata=args.add_metadata,
        lower_pathname=args.lower_pathname,
        lower_filename=args.lower_filename,
        line_break=args.line_break,
    ).get_notion_pages_from_database(
        database_url=args.database_url,
        category_column_name=args.category_column_name,
        tags_column_name=args.tags_column_name,
        created_time_column_name=args.created_time_column_name,
        status_column_name=args.status_column_name,
        current_status=args.current_status,
        next_status=args.next_status,
        filters=args.filters,
    )
