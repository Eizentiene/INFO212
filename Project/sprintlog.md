# Sprint Log

## Sprint 1 (September 22–28)
### Day 1 - Project Setup & Repo Initialization
- Created GitHub repository  
- Set up environment
- Initialized repo
- Added .gitignore and sprint-log.md
- Cloned repo to local folder
To do: Set up virtual environment and folder structure

### Day 2 — Environment Setup
- Created and activated Python virtual environment
- Added folders for app and tests
- Added basic Transaction class and main app file
- Installed pytest for unit testing
To do: Implement basic add/view transaction functionality

### Day 3 - Transaction Input
- Implemented add_transaction() function
- Implemented view_transactions() function
- Updated main.py for user interaction
- Added test_main.py for unit testing
To do: Add persistence for transactions (save/load)

### Day 4 - Persistence
- Fixed float parsing (support decimal separator)
- Added save_transactions() and load_transactions() functions
To do: Test persistence
Impediments: Handling old transactions file format

### Day 5 - Verification
- Implemented add/view transactions
- Implemented save/load to transactions.txt
- Added and ran a simple unit test
- Verified transactions persist across runs
To do: Prepare for next Sprint enhancements



## Sprint 2 (September 29 - Oct 5)


### Day 1 - Planning MVP Enhancements
- Planned final MVP enhancements
- included date, categories, total balance, and CSV export
To do: Update code structure for new features

### Day 2 - Updating Data Model & CSV Export
- Updated Transaction class to include category and timestamp
- Updated main.py to handle new 4-column transaction format
- Added export_to_csv() function
To do: Add improved display for transactions

### Day 3 - Enhanced Display & Balance
- Implemented color-coded amounts in 
- view_transactions() (green for positive, red for negative)
- Added view_balance() for total balance summary
To do: Test all features together

### Day 4 - Testing & Fixes
- Tested full MVP: add/view transactions, CSV export, total balance, color-coded output
- Fixed old transactions.txt format issues (removed old file)
To do: Final verification for submission
Impediments: Old file format required cleanup

### Day 5 - Final Verification & Submission Preparation
- Final verification of all features
- Prepared requirements.txt and ensured virtual environment works
- Added notes for submission PDF
To do: Submit PDF

- Optional improvements noted for next iteration:
  *Allow deleting transactions
  *Summary per category
  *Enhanced CLI interface
  *More unit tests for save/load

