#!/usr/bin/env python3
"""
freee API CLI Tool

Command-line interface for calling freee API endpoints directly.
Provides a simple way to interact with freee API from the command line.

Usage:
    freee_api.py <METHOD> <PATH> [OPTIONS]

Examples:
    # GET request
    freee_api.py GET /api/1/users/me
    freee_api.py GET /api/1/companies

    # GET with query parameters
    freee_api.py GET /api/1/deals -p '{"company_id": 123456}'

    # POST request
    freee_api.py POST /api/1/expense_applications \\
        -d '{"company_id": 123456, "title": "Transportation"}'

    # PUT request
    freee_api.py PUT /api/1/deals/789 -d '{"memo": "Updated"}'

    # DELETE request
    freee_api.py DELETE /api/1/deals/789

    # Output raw JSON (no formatting)
    freee_api.py GET /api/1/users/me --raw

Dependencies:
    - freee_session.py (must be in the same directory)
"""

import sys
import json
import argparse
from pathlib import Path

# Import FreeeSession from the same directory
try:
    from freee_session import FreeeSession, FreeeSessionError, AuthenticationError, APIError
except ImportError:
    print("[ERROR] Cannot import freee_session module")
    print("Make sure freee_session.py is in the same directory as this script")
    sys.exit(1)


def parse_json_arg(json_str):
    """
    Parse JSON string argument

    Args:
        json_str: JSON string or None

    Returns:
        Parsed dict or None

    Raises:
        ValueError: If JSON parsing fails
    """
    if json_str is None:
        return None

    try:
        return json.loads(json_str)
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON: {e}")


def format_output(data, raw=False):
    """
    Format API response for output

    Args:
        data: Response data (dict or other)
        raw: If True, output compact JSON without formatting

    Returns:
        Formatted string
    """
    if raw:
        return json.dumps(data, ensure_ascii=False)
    else:
        return json.dumps(data, indent=2, ensure_ascii=False)


def main():
    """Main CLI entry point"""
    parser = argparse.ArgumentParser(
        description='Call freee API from command line',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s GET /api/1/users/me
  %(prog)s GET /api/1/deals -p '{"company_id": 123456}'
  %(prog)s POST /api/1/expense_applications -d '{"company_id": 123456, "title": "Travel"}'
  %(prog)s PUT /api/1/deals/789 -d '{"memo": "Updated"}'
  %(prog)s DELETE /api/1/deals/789
  %(prog)s GET /api/1/users/me --raw
        """
    )

    parser.add_argument(
        'method',
        choices=['GET', 'POST', 'PUT', 'DELETE'],
        help='HTTP method to use'
    )

    parser.add_argument(
        'path',
        help='API endpoint path (e.g., /api/1/users/me)'
    )

    parser.add_argument(
        '-p', '--params',
        help='Query parameters as JSON string (e.g., \'{"company_id": 123456}\')'
    )

    parser.add_argument(
        '-d', '--data',
        help='Request body as JSON string (e.g., \'{"title": "Example"}\')'
    )

    parser.add_argument(
        '--raw',
        action='store_true',
        help='Output raw JSON without formatting'
    )

    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Show verbose output including request details'
    )

    args = parser.parse_args()

    # Parse JSON arguments
    try:
        params = parse_json_arg(args.params)
        data = parse_json_arg(args.data)
    except ValueError as e:
        print(f"[ERROR] {e}", file=sys.stderr)
        sys.exit(1)

    # Validate arguments
    if args.method == 'GET' and args.data:
        print("[WARNING] --data is ignored for GET requests", file=sys.stderr)
        data = None

    if args.method in ['POST', 'PUT'] and not args.data:
        print(f"[WARNING] {args.method} request without --data", file=sys.stderr)

    # Show request details if verbose
    if args.verbose:
        print(f"[REQUEST] {args.method} {args.path}", file=sys.stderr)
        if params:
            print(f"[PARAMS] {params}", file=sys.stderr)
        if data:
            print(f"[DATA] {data}", file=sys.stderr)

    # Initialize session
    try:
        session = FreeeSession()
    except Exception as e:
        print(f"[ERROR] Failed to initialize session: {e}", file=sys.stderr)
        sys.exit(1)

    # Make API request
    try:
        if args.method == 'GET':
            result = session.get(args.path, params=params)
        elif args.method == 'POST':
            result = session.post(args.path, json_data=data)
        elif args.method == 'PUT':
            result = session.put(args.path, json_data=data)
        elif args.method == 'DELETE':
            result = session.delete(args.path)
        else:
            print(f"[ERROR] Unsupported method: {args.method}", file=sys.stderr)
            sys.exit(1)

        # Output result
        print(format_output(result, raw=args.raw))

    except AuthenticationError as e:
        print(f"[AUTHENTICATION ERROR] {e}", file=sys.stderr)
        print("", file=sys.stderr)
        print("Please check:", file=sys.stderr)
        print("1. Configuration file: ~/.config/freee-skill/config.json", file=sys.stderr)
        print("2. Run authentication: session.authenticate()", file=sys.stderr)
        sys.exit(1)

    except APIError as e:
        print(f"[API ERROR] {e}", file=sys.stderr)
        if hasattr(e, 'status_code'):
            print(f"Status code: {e.status_code}", file=sys.stderr)
        if hasattr(e, 'response_data'):
            print(f"Response: {format_output(e.response_data, raw=args.raw)}", file=sys.stderr)
        sys.exit(1)

    except FreeeSessionError as e:
        print(f"[ERROR] {e}", file=sys.stderr)
        sys.exit(1)

    except KeyboardInterrupt:
        print("\n[INTERRUPTED] Request cancelled by user", file=sys.stderr)
        sys.exit(130)

    except Exception as e:
        print(f"[UNEXPECTED ERROR] {e}", file=sys.stderr)
        if args.verbose:
            import traceback
            traceback.print_exc(file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
