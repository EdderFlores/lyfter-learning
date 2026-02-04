#!/usr/bin/env python3
"""
TurFresh Complete Review Parser
Extracts all ~571 reviews from the 2025 Google reviews document
Generates a complete CSV file with all review data

Usage:
    python turfresh_complete_parser.py input_document.txt output_reviews.csv
"""

import csv
import re
import sys


def parse_reviews_from_text(text):
    """
    Parse all TurFresh reviews from the document text.
    
    Document structure per review:
    [Initials - 1-3 letters]
    Google
    [Reviewer Name]
    [Location - "TurFresh - City, State" or just "TurFresh"]
    [Stars - line with "full-star" repeated]
    [Numeric rating - single digit]
    [Date - e.g., "Dec 31st, 2025, 4:58am"]
    [Review text - optional, can be multiple lines]
    TurFresh
    [Reply date]
    [Reply text - multiple lines]
    """
    
    lines = text.strip().split('\n')
    reviews = []
    i = 0
    
    while i < len(lines):
        line = lines[i].strip()
        
        # Look for "Google" which marks the start of a review
        if line == "Google":
            review = {}
            
            # Get reviewer name (next line after Google)
            i += 1
            if i < len(lines):
                review['reviewer_name'] = lines[i].strip()
            
            # Get location
            i += 1
            if i < len(lines):
                location = lines[i].strip()
                review['location'] = location if 'TurFresh' in location else 'TurFresh'
            
            # Get stars (count "full-star" occurrences)
            i += 1
            if i < len(lines):
                star_line = lines[i].strip()
                star_count = star_line.count('full-star')
                review['stars'] = star_count if star_count > 0 else 5
            
            # Skip numeric rating line
            i += 1
            if i < len(lines) and lines[i].strip().isdigit():
                i += 1
            
            # Get review date
            if i < len(lines):
                review['review_date'] = lines[i].strip()
                i += 1
            
            # Collect review text (until "TurFresh" reply marker or next review)
            review_text_lines = []
            while i < len(lines):
                current = lines[i].strip()
                
                # Check if we hit the reply marker
                if current == "TurFresh":
                    # Get reply date
                    i += 1
                    if i < len(lines):
                        review['reply_date'] = lines[i].strip()
                        i += 1
                    
                    # Collect reply text
                    reply_lines = []
                    while i < len(lines):
                        reply_current = lines[i].strip()
                        
                        # Check if next review is starting
                        # (short initials followed by "Google" on next line)
                        if i + 1 < len(lines):
                            next_line = lines[i+1].strip()
                            if next_line == "Google" and len(reply_current) <= 5:
                                # This is the initials of the next review
                                break
                        
                        if reply_current:
                            reply_lines.append(reply_current)
                        i += 1
                    
                    review['reply_text'] = ' '.join(reply_lines)
                    break
                
                # Check if next review starting (next line is "Google")
                if i + 1 < len(lines) and lines[i+1].strip() == "Google":
                    # Current line might be initials
                    break
                
                # Skip lines that look like initials (short uppercase codes)
                if current and not (len(current) <= 5 and current.replace('"', '').replace("'", "").isupper()):
                    review_text_lines.append(current)
                
                i += 1
            
            review['review_text'] = ' '.join(review_text_lines)
            
            # Only add if we have at least a reviewer name
            if 'reviewer_name' in review:
                # Ensure all fields exist
                review.setdefault('review_date', '')
                review.setdefault('location', 'TurFresh')
                review.setdefault('stars', 5)
                review.setdefault('review_text', '')
                review.setdefault('reply_text', '')
                review.setdefault('reply_date', '')
                
                reviews.append(review)
        else:
            i += 1
    
    return reviews


def save_reviews_to_csv(reviews, output_file):
    """Save parsed reviews to CSV file."""
    fieldnames = [
        'reviewer_name',
        'review_date',
        'location',
        'stars',
        'review_text',
        'reply_text',
        'reply_date'
    ]
    
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        
        for review in reviews:
            writer.writerow({
                'reviewer_name': review.get('reviewer_name', ''),
                'review_date': review.get('review_date', ''),
                'location': review.get('location', ''),
                'stars': review.get('stars', ''),
                'review_text': review.get('review_text', ''),
                'reply_text': review.get('reply_text', ''),
                'reply_date': review.get('reply_date', '')
            })
    
    return len(reviews)


def main():
    """Main execution function."""
    if len(sys.argv) < 3:
        print("Usage: python turfresh_complete_parser.py <input_file.txt> <output_file.csv>")
        print()
        print("Example:")
        print("  python turfresh_complete_parser.py reviews_2025.txt turfresh_reviews_complete.csv")
        print()
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    print("TurFresh Complete Review Parser")
    print("=" * 70)
    print()
    print(f"Input file: {input_file}")
    print(f"Output file: {output_file}")
    print()
    print("Reading document...")
    
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            document_text = f.read()
    except FileNotFoundError:
        print(f"ERROR: Could not find file '{input_file}'")
        sys.exit(1)
    except Exception as e:
        print(f"ERROR: Could not read file: {e}")
        sys.exit(1)
    
    print("Parsing reviews...")
    reviews = parse_reviews_from_text(document_text)
    
    print(f"Found {len(reviews)} reviews")
    print()
    print("Saving to CSV...")
    
    try:
        count = save_reviews_to_csv(reviews, output_file)
        print(f"✓ Successfully saved {count} reviews to {output_file}")
        print()
        print("Sample of extracted data:")
        print("-" * 70)
        for i, review in enumerate(reviews[:3], 1):
            print(f"\nReview {i}:")
            print(f"  Name: {review['reviewer_name']}")
            print(f"  Date: {review['review_date']}")
            print(f"  Location: {review['location']}")
            print(f"  Stars: {review['stars']}")
            print(f"  Has review text: {'Yes' if review['review_text'] else 'No'}")
            print(f"  Has reply: {'Yes' if review['reply_text'] else 'No'}")
        print()
        print("=" * 70)
        print("COMPLETE! CSV file ready to use.")
    except Exception as e:
        print(f"ERROR: Could not save CSV: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()