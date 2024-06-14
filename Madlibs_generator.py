def new_story():
    with open("story.txt","r") as f:
        word=f.read()
        return word
words=set()    
story=new_story()
start_point="<"
end_point=">"
start_index=-1
for i,c in enumerate(story):
    if c==start_point:
        start_index=i
    if c==end_point and start_index!= -1:
        word=story[start_index:i+1]
        words.add(word)
        
characters={}
for i in words:
    values=input("Give values to the "+i)
    characters[i]=values
    
for word in words:
    story=story.replace(word,characters[word])
                 
print(story)              