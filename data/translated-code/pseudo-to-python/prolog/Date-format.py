from datetime import datetime

# Step 2
current_time = datetime.now()

# Step 3
Short = current_time.strftime('%Y-%m-%d')

# Step 4
Long = current_time.strftime('%A, %B %d, %Y')

# Step 5
print(Short)
print(Long)