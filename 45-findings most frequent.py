from collections import Counter

text="Facebook is an American for-profit corporation and online social media and social networking service"\
    "The founders had initially limited the website's membership to Harvard students; however, later they expanded it to higher education "\
    "Facebook may be accessed by a large range of desktops, laptops, tablet computers, and smartphones over the Internet and mobile "\
    "Facebook, Inc. held its initial public offering (IPO) in February 2012, and began selling stock to the public three months later."

words=text.split()
print(words)

counter=Counter(words)
top_three=counter.most_common(3)
print(top_three)