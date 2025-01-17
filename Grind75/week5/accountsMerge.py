class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        # Sort accounts by the name (first element of each account)
        accounts = sorted(accounts, key=lambda x: x[0])
        
        # Merge function to combine emails from two accounts
        def merge(acc1, acc2):
            # Merge the emails (using a set to avoid duplicates)
            merged_emails = set(acc1[1:] + acc2[1:])
            merged_emails = sorted(merged_emails)  # Sort emails lexicographically
            return [acc1[0]] + merged_emails  # Return the name and sorted emails
        
        # Iterate over the accounts to merge them
        i = 0
        while i < len(accounts):
            j = i + 1
            while j < len(accounts):
                # Check if both accounts share the same name
                if accounts[i][0] == accounts[j][0]:
                    # Check if they share any email (from second email onwards)
                    shared_email = False
                    for email in accounts[i][1:]:
                        if email in accounts[j]:
                            shared_email = True
                            break
                    
                    # If they share an email, merge the accounts
                    if shared_email:
                        accounts[i] = merge(accounts[i], accounts[j])
                        # Remove the j-th account as it has been merged
                        del accounts[j]
                    else:
                        # Move to the next account if they don't share an email
                        j += 1
                else:
                    # Move to the next account if the names are different
                    j += 1
            
            # Move to the next account
            i += 1
        
        return accounts