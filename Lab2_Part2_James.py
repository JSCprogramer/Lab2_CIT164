#making code o convert seconds to minutes with reminder#

seconds=int(input("Enter seconds to convert:"))

minutes=seconds // 60
remaining_seconds=seconds%60
#if you want a variable used in {} or dynamic variables use f" to format it#
print(f"{seconds} seconds is equal to {minutes}  minutes and {remaining_seconds} seconds.")

