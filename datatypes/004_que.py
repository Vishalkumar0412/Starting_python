# Given data
population = 80000
total_men = (population * 52) // 100
total_women = population - total_men
literate_all = (population * 48) // 100
literate_men = (population * 35) // 100

# Findings
illiterate_all = population - literate_all
literate_women = literate_all - literate_men
illiterate_men = total_men - literate_men
illiterate_women = total_women - literate_women

# Print results
print("Total Population:", population)
print("Total Men:", total_men)
print("Total Women:", total_women)
print("Literate People:", literate_all)
print("Illiterate People:", illiterate_all)
print("Literate Men:", literate_men)
print("Literate Women:", literate_women)
print("Illiterate Men:", illiterate_men)
print("Illiterate Women:", illiterate_women)
