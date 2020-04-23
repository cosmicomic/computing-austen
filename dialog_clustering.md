## Clustering Dialog

I wanted to get a feel for sentences generated purely from dialog vs. sentences generated purely from narration (see other file). Dialog was isolated using a regular expression. This was done very coarsely: basically any text surrounded by quotation marks was appended to one big dialog string, and then that string was processed by the clustering algorithm. For example, if a piece of dialog looked like this:

> "X," said Mary. "Y."
> 
> "Z," said Jane.
> 
> "W."

It would be added to the mass dialog string simply as "X. Y. Z. W." No distinction is made between speakers, and dialog is not grouped by conversation or speaker.

This is not very useful for simulating conversations, where there will be two or more distinct speakers, and there is some meaningful sequence of utterances spoken by the different speakers. 

## The Clusters ##

### Cluster 0 ###
-   If you value her conduct or happiness, infuse as much of your own spirit into her as you can
-   What have they brought you
-  Are you serious
-   We are quite near relations, you know; and Mr Elliot too, whom you ought so particularly to be acquainted with
-   I will only tell you what I have found him

### Cluster 1 ###
-   My dearest Anne, it would give me more delight than is often felt at my time of life
-  More air than one often sees in Bath
-   She saw no reason against their being happy
-  Oh
-   The usual character of them has nothing for me

### Cluster 2 ###
-  I am almost ashamed to say it
-  We sailors, Miss Elliot, cannot afford to make long courtships in time of war
-  Believe it to be most fervent, most undeviating, in F
- I have let my house to Admiral Croft, A few months more, and he, perhaps, may be walking here
-  Lady Russell took her out in her carriage almost every morning, and she never failed to think of them, and never failed to see them

### Cluster 3 ###
-  The Crofts knew quite as many people in Bath as they wished for, and considered their intercourse with the Elliots as
a mere matter of form, and not in the least likely to afford them any pleasure
-  Then she had, indeed, been a pitiable object; for she had caught cold on the journey, and had hardly taken possession
of her lodgings before she was again confined to her bed and suffering under severe and constant pain; and all this amon
g strangers, with the absolute necessity of having a regular nurse, and finances at that moment particularly unfit to meet any extraordinary expense
- on Tuesday night, he made a very awkward sort of excuse; 'he never shot' and he had 'been quite misunderstood,' and he
had promised this and he had promised that, and the end of it was, I found, that he did not mean to come
-  To begin without knowing that at such a time there will be the means of marrying, I hold to be very unsafe and unwise,
 and what I think all parents should prevent as far as they can
  I suppose he was afraid of finding it dull; but upon my word I should have thought we were lively enough at the Cottage for such a heart-broken man as Captain Benwick
## Generated Sequences ##


state sequence = 2, 2, 3, 3, 2

But, Captain Wentworth, how vexed you must have been obliged to give Miss Anne's message. No, I believe you equal to every risk and hardship. They have no right to be at Lyme. Nursing does not recover from such a woman. I mean to have looked about me to Mr Elliot.


----------


state sequence = 3, 1, 1, 2, 2

Very well, I have nothing to alarm you. And take it for a time, with the liberality of a second visit she talked with great openness, and Anne's astonishment increased. When you had seen lent about among half your acquaintance ever since the death of that nature in the least likely to do him good. Though I came to the purpose, You were not formerly, I know.
I have read your feelings, as I did, unless you had been influenced by any one rather than by me.

----------

state sequence = 0, 2, 2, 2, 3

But now, do not think Charles might as well as read. You are never sure of a good account of yourself on Thursday. If you value her conduct or happiness, infuse as much of your sister are gone; and what he is dear to us. You would not see her behaviour. I happened to be added to all this, much may be done.