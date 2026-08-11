# Playing for Real A Text on Game Theory Ken Binmore

Playing for Real

A Text on Game Theory

Ken Binmore

Oxford University Press, Inc., publishes works that further Oxford University’s objective of excellence in research, scholarship, and education.

Oxford New York

Auckland Cape Town Dares Salaam Hong Kong Karachi Kuala Lumpur Madrid Melbourne Mexico City Nairobi New Delhi Shanghai Taipei Toronto

With offices in

Argentina Austria Brazil Chile Czech Republic France Greece Guatemala Hungary Italy Japan Poland Portugal Singapore South Korea Switzerland Thailand Turkey Ukraine Vietnam

Oxford is a registered trademark of Oxford University Press

Library of Congress Cataloging-in-Publication Data

1 3 5 7 9 8 6 4 2

I dedicate Playing for Real to my wife, Josephine

Preface

There are at least three questions a game theory book might answer: What is game theory about? How do I apply game theory? Why is game theory right?

Playing for Real tries to answer all three questions. I think it is the only book that makes a serious attempt to do so without getting heavily mathematical. There are elementary books that offer students the opportunity to admire some game theory concepts. There are cookbooks that run through lots of applied models. There are philosophical works that supposedly address the foundational issues, but none of these address more than two of the questions.

However, answering questions is only part of what this book is about. Just as athletes take pleasure in training their bodies, so there is immense satisfaction to be found in training your mind to think in a way that is simultaneously rational and creative. With all of its puzzles and paradoxes, game theory provides a magnificent mental gymnasium for this purpose. I hope that exercising on the equipment will bring you the same kind of pleasure it has brought me.

Moving on. Playing for Real isn’t my first textbook on game theory. My earlier book, Fun and Games, was used quite widely for teaching advanced undergraduate and beginning graduate students. I had originally planned a modestly revised second edition, in which the rather severe introduction would be replaced with a new chapter that would ease students into the subject by running through all the angles on the Prisoners’ Dilemma. The remaining chapters were then simply to be broken down into more digestible chunks. But the project ran away with me. I made the improvements I planned to make but somehow ended up with a whole new book.

There are two reasons why. The first is that game theory has moved on since I wrote Fun and Games. Some of the decisions on what material to include that seemed a little daring at the time now look totally uncontroversial. So I have tried my luck at guessing which way the subject is going to jump again.

The second reason is that I have moved on as well. In particular, I have done a great deal of consulting work, applying game theory to real-world problems in order to raise money for my research center. The biggest project was the design of a telecom auction that raised $35 billion. I always knew that game theory works, but seeing it triumph on such a scale was beyond all expectation! I have also written a book applying game theory to philosophical issues, which taught me a great deal about how and why beginners make mistakes when thinking about strategic issues. Both kinds of experience have contributed to making Playing for Real a better book than its predecessor. My flirtation with philosophy even generated a lot of light-hearted exercises that nevertheless make genuinely serious points.

Material. As a text on game theory for undergraduates with some mathematical training, Playing for Real improves on Fun and Games in a number of ways. It continues to be suitable for courses attended by students from a variety of disciplines. (Some of my very best undergraduates at the University of Michigan were from Classics.) It also continues to provide backup sections on the necessary mathematics, so that students whose skills are rusty can keep up with what’s going on without too much effort. However, the book as a whole covers fewer basic topics in a more relaxed and discursive style, with many more examples and economic applications.

I hope the opening chapter, which uses the Prisoners’ Dilemma to provide an undemanding overview of what game theory is all about, will prove to be a particularly attractive feature. Economists will also be pleased to see a whole chapter devoted to the theory of imperfect competition, where I believe I may even have made Bertrand-Edgeworth competition accessible to undergraduates. It is a tragedy that evolutionary game theory had to go, but this important subject has gotten so big that it deserves a whole book to itself.

Although fewer topics are covered, some topics are covered in much more detail than in Fun and Games. These include cooperative game theory, Bayesian decision theory, games of incomplete information, mechanism design, and auction theory, each of which now has its own chapter. However, the theory of bargaining has grown more than anything else, partly because I hope to discourage various misunderstandings of the theory that have become commonplace in applied work, and partly because I wanted to illustrate its potential use in ethics and moral philosophy.

Teaching. There is enough material in this book for at least two courses in game theory, even leaving aside the review and other sections that are intended for private reading. I have tried to make things easy for teachers who want to design a course based on a selection of topics from the whole book by including marginal notes to facilitate skipping. For example, the Mad Hatter, who has appeared in the margin, suggests skipping on to the first chapter, on the grounds that there is too much philosophy in this preface.

The exercises are similarly labeled with warnings about their content. Nobody will want to attempt all of the enormous number of exercises, but when I teach, I insist on students trying a small number of carefully chosen exercises every week. Once they get into the habit, students are often surprised to find that solving problems can be a lot of fun.

By the time the book is published, Jernej Copic will have finished getting his solutions onto a website. Oxford University Press will provide access details to recognized teachers.

Thanks. So many people have helped me, with both Fun and Games and Playing for Real, that I have lost track of them all. I shall therefore mention only the very special debt of gratitude I owe to my long-time coauthor, Larry Samuelson, for both his patience and his encouragement. I also want to thank the California Institute of Technology for giving me the leisure to complete this book as a Gordon Moore Scholar. I should also acknowledge the Victorian artist John Tenniel, whose magnificent illustrations from Lewis Carroll’s Alice books I have shamelessly stolen and messed around with.

Finally, I need to apologize not only for my mistakes but also for my attempts at humor. Oscar Wilde reported that a piano in a Western saloon carried a notice saying, ‘‘Please don’t shoot the pianist. He’s doing his best.’’ The same goes for me, too. It isn’t easy to write in a light-hearted style when presenting mathematical material, but I did my best.

Ken Binmore

Contents

1 Getting Locked In 1 2 Backing Up 39 3 Taking Chances 77 4 Accounting for Tastes 111 5 Planning Ahead 143 6 Mixing Things Up 177 7 Fighting It Out 215 8 Keeping Your Balance 253 9 Buying Cheap 273 10 Selling Dear 299 11 Repeating Yourself 319 12 Getting the Message 353 13 Keeping Up to Date 383 14 Seeking Refinement 407 15 Knowing What to Believe 431 16 Getting Together 459 17 Cutting a Deal 493 18 Teaming Up 521 19 Just Playing? 543 20 Taking Charge 567 21 Going, Going, Gone! 593

Getting Locked In

## 1.1 What Is Game Theory?

A game is being played whenever people have anything to do with each other. Romeo and Juliet played a teenage mating game that didn’t work out too well for either of them. Adolf Hitler and Josef Stalin played a game that killed off a substantial fraction of the world’s population. Kruschev and Kennedy played a game during the Cuban missile crisis that might have wiped us out altogether.

Drivers maneuvering in heavy traffic are playing a game with the drivers of the other cars. Art lovers at an auction are playing a game with the rival bidders for an old master. A firm and a union negotiating next year’s wage contract are playing a bargaining game. When the prosecuting and defending attorneys in a murder trial decide what arguments to put before the jury, they are playing a game. A supermarket manager deciding today’s price for frozen pizza is playing a game with all the other storekeepers in the neighborhood with pizza for sale.

If all of these scenarios are games, then game theory obviously has the potential to be immensely important. But game theorists don’t claim to have answers to all of the world’s problems because the orthodox game theory to which this book is devoted is mostly about what happens when people interact in a rational manner. So it can’t predict the behavior of love-sick teenagers like Romeo or Juliet or madmen like Hitler or Stalin. However, people don’t always behave irrationally, and so it isn’t a waste of time to study what happens when we are all wearing our thinking caps. Most of us at least try to spend our money sensibly—and we don’t do too badly at it most of the time.

badly much of the time; otherwise, economic theory wouldn’t work at all.

Even when people haven’t actively thought things out in advance, it doesn’t necessarily follow that they are behaving irrationally. Game theory has had some notable successes in explaining the behavior of insects and plants, neither of which can be said to think at all. They end up behaving rationally because those insects and plants whose genes programmed them to behave irrationally are now extinct. Similarly, companies may not always be run by great intellects, but the market can sometimes be just as ruthless as Nature in eliminating the unfit from the scene.

## 1.2 Toy Games

Rational interaction within groups of people may be worth studying, but why call it game theory? Why trivialize the problems that people face by calling them games? Don’t we devalue our humanity by reducing our struggle for fulfillment to the status of mere play in a game?

Game theorists answer such questions by standing them on their heads. The more deeply we feel about issues, the more we need to strive to avoid being misled by wishful thinking. Game theory makes a virtue out of using the language of parlor games like chess or poker so that we can discuss the logic of strategic interaction dispassionately.

Bridge players have admittedly been known to shoot their partners. I have sometimes felt the urge myself. But most of we are able to contemplate the strategic problems that arise in parlor games without getting emotionally involved. It then becomes possible to follow the logic wherever it leads, without throwing our hands up in denial when it takes us somewhere we would rather not go. When game theorists use the language of parlor games in analyzing serious social problems, they aren’t therefore revealing themselves to be heartless disciples of Machiavelli. They are simply doing their best to separate those features of a problem that admit an uncontroversial rational analysis from those that don’t.

This introductory chapter goes even farther down this path by confining its attention to toy games. In studying a toy game, we seek to sweep away all the irrelevant clutter that typifies real-world problems, so that we can focus our attention entirely on the basic strategic issues. To distance the problem even further from the prejudices with which we are all saddled, game theorists usually introduce toy games with silly stories that would be more at home in Alice in Wonderland than in a serious work of social science. But although toy games get discussed in a playful spirit, it would be a bad mistake to dismiss them as too frivolous to be worthy of serious attention.

Our untutored intuition is notoriously unreliable in strategic situations. If Adam and Eve are playing a game, then Adam’s choice of strategy will depend on what strategy he predicts Eve will choose. But she must simultaneously choose a strategy, using her prediction of Adam’s strategy choice. Given that it is necessarily based on such circular reasoning, it isn’t surprising that game theory abounds with surprises and paradoxes. We therefore need to sharpen our wits by trying to understand really simple problems before attempting to solve their complicated cousins.

Nobody ever solved a genuinely difficult problem without trying out their ideas on easy problems first. The crucial step in solving a real-life strategic problem nearly always consists of locating a toy game that lies at its heart. Only when this has been solved does it make sense to worry about how its solution needs to be modified to take account of all the bells and whistles that complicate the real world.

## 1.3 The Prisoners’ Dilemma

The Prisoners’ Dilemma is the most famous of all toy games. People so dislike the conclusion to which game-theoretic reasoning leads in this game that an enormous literature has grown up that attempts to prove that game theory is hopelessly wrong. There are two reasons for beginning Playing for Real with a review of some of the fallacies invented in this critical literature. The first is to reassure readers that the simple arguments game theorists offer must be less trivial than they look. If they were obvious, why would so many clever people have thought it worthwhile to spend so much time trying to prove them wrong? The second reason is to explain why later chapters take such pains to lay the foundations of game theory with excruciating care. We need to be crystal clear about what everything in a game-theoretic model means—otherwise we too will make the kind of mistakes we will be laughing at in this chapter.

1.3.1 Chicago Times

The original story for the Prisoners’ Dilemma is set in Chicago. The district attorney knows that Adam and Eve are gangsters who are guilty of a major crime but is unable to convict either unless one of them confesses. He orders their arrest and separately offers each the following deal: If you confess and your accomplice fails to confess, then you go free. If you fail to confess but your accomplice confesses, then you will be convicted and sentenced to the maximum term in jail. If you both confess, then you will both be convicted, but the maximum sentence will not be imposed. If neither confesses, you will both be framed on a minor tax evasion charge for which a conviction is certain.

In such problems, Adam and Eve are the players in a game. In the toy game called the Prisoners’ Dilemma, each player can choose one of two strategies, called hawk and dove. The hawkish strategy is to fink on your accomplice by confessing to the crime. The dovelike strategy is to stick by your accomplice by holding out against a confession.

Game theorists assess what might happen to a player by assigning payoffs to each possible outcome of the game. The context in which the Prisoners’ Dilemma is posed invites us to assume that neither player wants to spend more time in jail than necessary. We therefore measure how a player feels about each outcome of the game by counting the number of years in jail he or she will have to serve. These penalties aren’t given in the statement of the problem, but we can invent some appropriate numbers.

If Adam holds out and Eve confesses, the strategy pair (dove, hawk) will be played. Adam is found guilty and receives the maximum penalty of 10 years in jail. We record this result by making Adam’s payoff for (dove, hawk) equal to -10. If Eve holds out and Adam confesses, (hawk, dove) is played. Adam goes free, and so his payoff for (hawk, dove) is 0. If Adam and Eve both hold out, the outcome is (dove, dove). In this case, the district attorney trumped up a tax evasion charge against both players, and they each go to jail for one year. Adam’s payoff for (dove, dove) is therefore -1. If Adam and Eve both confess, the outcome is (hawk, hawk). Each is found guilty, but since confession is a mitigating circumstance, each receives a penalty of only 9 years. Adam’s payoff for (hawk, hawk) is therefore -9.

The payoffs chosen for Adam in the Prisoners’ Dilemma are shown as a payoff matrix in Figure 1.1(a). His strategies are represented by the rows of the matrix. Eve’s strategies are represented by its columns. Each cell in the matrix represents a possible outcome of the game. For example, the top-right cell corresponds to the outcome (dove, hawk), in which Adam plays dove and Eve plays hawk. Adam goes to jail for 10 years if this outcome occurs, and so -10 is written inside the top-right cell of his payoff matrix.

Eve’s payoff matrix is shown in Figure 1.1(b). Although the game is symmetric, her payoff matrix isn’t the same as Adam’s. To get Eve’s matrix, we have to swap the rows and columns in Adam’s matrix. In mathematical jargon, her matrix is the transpose of his.

Figure 1.2(a) shows both players’ payoff matrices written together. The result is called the payoff table for the Prisoners’ Dilemma. Adam’s payoff appears in the southwest corner of a cell and Eve’s in the northeast corner. For example, -1 is written in the southwest corner of the top-left cell because this is Adam’s payoff if both players choose dove. Similarly, -9 is written in the north-east corner of the bottom-right cell because this is Eve’s payoff if both players choose hawk.

The problem for the players in a game is that they usually don’t know what strategy their opponent will choose. If they did, they would simply reply by choosing whichever of their own strategies would then maximize their payoff.

1 Although its entries are vectors rather than scalars, such a table is often called the payoff matrix of the game. Sometimes it is called a bimatrix to indicate that it is really two matrices written together. Most game theorists write the payoffs on one line, so the entry in the cell (hawk, hawk) would be (-9, -9). Beginners seem to find my representation less confusing. Thomas Schelling tells me that he has carried out experiments which confirm that payoff tables written in this way reduce the number of mistakes that get made.

For example, if Adam knew that Eve were sure to choose dove in the Prisoners’ Dilemma, then he would only need to look at his payoffs in the first column of his payoff matrix. These payoffs are -1 and 0. The latter is circled in Figures 1.1(a) and 1.2(a) because it is bigger. The circle therefore indicates that Adam’s best reply to Eve’s choice of dove is to play hawk. Similarly, if Adam knew that Eve were sure to choose hawk, then he would only need to look at his payoffs in the second column of his payoff matrix. These payoffs are -10 and -9. The latter is circled in Figures 1.1(a) and 1.2(a) because it is bigger. Adam’s best reply to Eve’s choice of hawk is therefore to play hawk.

In most games, Adam’s best reply depends on which strategy he guesses that Eve will choose. The Prisoners’ Dilemma is special because Adam’s best reply is necessarily the same whatever strategy Eve may choose. He therefore doesn’t need to know or guess what strategy she will use in order to know what his best reply should be. He should never play dove because his best reply is always to play hawk, whatever Eve may do. Game theorists express this fact by saying that hawk strongly dominates dove in the the Prisoners’ Dilemma.

Since Eve is faced by exactly the same dilemma as Adam, her best reply is also always to play hawk, whatever Adam may do. If both Adam and Eve act to maximize their payoffs in the Prisoners’ Dilemma, each will therefore play hawk. The result will therefore be that both confess, and hence each will spend nine years in jail—whereas they could have gotten away with only one year each in jail if they had both held out and refused to confess.

People sometimes react to this analysis by complaining that the story of the district attorney and the gangsters is too complicated to be adequately represented by a simple payoff table. However, this complaint misses the point. Nobody cares about the story used to introduce the game. The chief purpose of such stories is to help us remember the relative sizes of the players’ payoffs. Moreover, the precise value of the payoffs we write into a table does not usually matter very much. We are interested in the strategic problem embodied in the payoff table rather than the details of some silly story. Any payoff table with the same strategic structure as Figure 1.2(a) would therefore suit us equally well, regardless of the story from which it was derived.

Figure 1.2(b) is the general payoff table for a Prisoners’ Dilemma. We need a > b and c > d to ensure that hawk strongly dominates dove. We need b > c to ensure that both players would get more if they both played dove instead of both playing hawk.

Critics of game theory don’t like our analysis of the Prisoners’ Dilemma because they see that Adam and Eve would both be better off if they came to an agreement to play dove. Neither would then confess, and so each would go to jail for only one year.

Naive critics think that this observation is enough to formulate an unassailable argument. They say that there are two theories of rational play to be compared. Their theory recommends that everybody should play dove in the Prisoners’ Dilemma. Game theory recommends that everybody should play hawk. If Alice and Bob play according to the naive theory, each will go to jail for only one year. If Adam and Eve play according to game theory, each will go to jail for nine years. So their theory outperforms ours.

There is admittedly much to be said for asking people who claim to be clever, ‘‘If you’re so smart, why ain’t you rich?’’ But when you compare how successful two people or two theories are, it is necessary to compare how well each performs under the same circumstances. After all, one wouldn’t say that Alice was a faster runner than Adam because she won a race in which she was given a head start. Let us therefore compare how well Alice and Adam will do when they play under the same conditions. First imagine what would happen if both were to play against Bob, and then imagine what would happen if both were to play against Eve.

When they play against Bob, Alice goes to jail for one year, and Adam for no years. So game theory wins on this comparison. When they play against Eve, Alice goes to jail for ten years, and Adam for nine years. So game theory wins this on this comparison as well. Game theory therefore wins all around when like is compared with like. Only when unlike is compared with unlike does it seem that the critics’ theory wins.

The trap that naive critics fall into is to let their emotions run away with their reason. They don’t like the conclusion to which one is led by game theory, and so they propose an alternative theory with nothing more to recommend it than the fact that it leads to a conclusion that they prefer. Game theorists also wish that rational play called for the play of dove in the Prisoners’ Dilemma. They too would prefer not to spend an extra eight years in jail. But wishing doesn’t make it so. As so often in this vale of tears, what we would like to be true is very different from what actually is true.

Of course, most critics are less naive. They continue to deny that game theory is right but recognize that there is a case to be answered by saying that the Prisoners’ Dilemma poses a paradox of rationality that desperately needs to be resolved. They get all worked up because they somehow convince themselves that the Prisoners’ Dilemma embodies the essence of the problem of human cooperation. If this were true, the game-theoretic argument, which denies that cooperation is rational in the Prisoners’ Dilemma, would imply that it is never rational for human beings to cooperate. This would certainly be dreadful, but it isn’t a conclusion that any game theorist would endorse.

Game theorists think it just plain wrong to claim that the Prisoners’ Dilemma embodies the essence of the problem of human cooperation. On the contrary, it represents a situation in which the dice are as loaded against the emergence of cooperation as they could possibly be. If the great game of life played by the human species were the Prisoners’ Dilemma, we wouldn’t have evolved as social animals! We therefore see no more need to solve some invented paradox of rationality than to explain why strong swimmers drown when thrown in Lake Michigan with their feet encased in concrete. No paradox of rationality exists. Rational players don’t cooperate in the Prisoners’ Dilemma because the conditions necessary for rational cooperation are absent in this game.

One of the many attempts to resolve the paradox of rationality supposedly posed by the Prisoners’ Dilemma tries to exploit the symmetry of the game by treating Adam and Eve as twins. It goes like this: Two rational people facing the same problem will come to the same conclusion. Adam should therefore proceed on the assumption that Eve will make the same choice as he. They will therefore either both go to jail for nine years, or they will both go to jail for one year. Since the latter is preferable, Adam should choose dove. Since Eve is his twin, she will reason in the same way and choose dove as well.

The argument is attractive because there are situations in which it would be correct. For example, it would be correct if Eve were Adam’s reflection in a mirror, or if Adam and Eve were genetically identical twins, and we were talking about what genetically determined behavior best promotes biological fitness (Section 1.6.2). However, the reason that the argument would then be correct is that the relevant game would no longer be the Prisoners’ Dilemma. It would be a game with essentially only one player.

As is commonplace when looking at fallacies of the Prisoners’ Dilemma, we find that we have been offered a correct analysis of some game that isn’t the Prisoners’ Dilemma. The Prisoners’ Dilemma is a two-player game in which Adam and Eve choose their strategies independently. Where the twins fallacy goes wrong is in assuming that Eve will make the same choice in the Prisoners’ Dilemma as Adam, whatever strategy he chooses. This can’t be right because one of Adam’s two possible choices is irrational. But Eve is an independent rational agent. She will behave rationally whatever Adam may do.

Insofar as it applies to the Prisoners’ Dilemma, the twins fallacy is correct only to the extent that rational reasoning will indeed lead Eve to make the same strategy choice as Adam if he chooses rationally. Game theorists argue that this choice will be hawk because hawk strongly dominates dove.

It is worth taking note of the twins fallacy at election time, when we are told that ‘‘every vote counts.’’ However, if a wasted vote is one that doesn’t affect the outcome of the election, then all votes are wasted—unless it turns out that only one vote separates the winner and the runner-up. If they are separated by two or more votes, then a change of vote by a single voter will make no difference at all to who is elected. But an election for a seat in a national assembly is almost never settled by a margin of only one vote. It is therefore almost certain that any particular vote in such an election will be wasted.

Since this is a view that naive people think might lead to the downfall of democracy, reasons have to be given as to why it is ‘‘incorrect.’’ We are therefore told that Adam is wrong to count only the impact that his vote alone will have on the outcome of the election; he should instead count the total number of votes cast by all those people who think and feel as he thinks and feels and hence will vote as he votes. If Adam has ten thousand such soulmates or twins, his vote would then be far from wasted because the probability that an election will be decided by a margin of ten thousand votes or less is often very high.

This argument is faulty for the same reason that the twins fallacy fails in the Prisoners’ Dilemma. There may be large numbers of people who think and feel like you, but their decisions on whether to go out and vote won’t change if you stay home and wash your hair.

Critics sometimes accuse game theorists of a lack of public spirit in exposing this fallacy, but they are wrong to think that democracy would fall apart if people were encouraged to think about the realities of the election process. Cheering at a football game is a useful analogy. Only a few cheers would be raised if what people were trying to do by cheering was to increase the general noise level in the stadium. No single voice can make an appreciable difference in how much noise is being made when a large number of people are cheering. But nobody cheers at a football game because they want to increase the general noise level. They shout words of wisdom and advice at their team even when they are at home in front of a television set.

Much the same goes for voting. You are kidding yourself if you vote because your vote may possibly be pivotal. However, it makes perfectly good sense to vote for the same reason that football fans yell advice at their teams. And, just as it is more satisfying to shout good advice rather than bad, so many game theorists think that you get the most out of participating in an election by voting as though you were going to be the pivotal voter, even though you know the probability of one vote making a difference is too small to matter (Section 13.2.4). Behaving in this way will sometimes result in your voting strategically for a minor party. The same pundits who tell you that every vote counts will also tell you that such a strategic vote is a wasted vote. But they can’t be allowed to have it both ways!

Before looking at more fallacies, it will be useful to tell another story that leads to the Prisoners’ Dilemma, so that we can get ourselves into an emotionally receptive state.

Private goods are commodities that people consume themselves. Public goods are commodities that can’t be provided without everybody being able to consume them. An army that prevents your country from being invaded provides a public good. National defense is a public good because it is impossible to defend only the people who pay for it. Everyone in the country benefits from the army, whether they contribute to its upkeep or not.

Country being invaded is an example. Streetlights are another. So are radio or television broadcasts. No matter who pays, everybody has access to a public good.

## 1.4 Private Provision of Public Goods

Our taxes pay for most public goods. Advertisers pay for others. But we are interested in the public goods that are paid for by voluntary subscription. Lighthouses were originally funded in this way. Charities still are. Universities depend on endowments from rich benefactors. Public television channels wouldn’t survive without the contributions made by their viewers. Young men offered their very lives for what they saw as the public good when volunteering in droves for various armies at the beginning of the First World War.

Utopians sometimes toy with the idea that all public goods should be funded by voluntary subscription. Economists then worry about the free rider problem. For example, if people can choose whether or not to buy a ticket when riding on trains, will enough people pay to cover the cost of running the system? Utopians shrug off this problem by arguing that people will see that it makes sense to pay because otherwise the train service will cease to run.

Free Rider Problem. The Prisoners’ Dilemma can be used to examine the free rider problem in a very simple case. A public good that is worth $3 each to Adam and Eve may or may not be provided at a cost of $2 per player. The public good is provided only if one or both of the players volunteer to contribute to the cost. If both volunteer, both pay their share of the cost. If only one player volunteers, he or she must pay both shares. Assuming that Adam and Eve care only about how much money they end up with, how will they play this game?

Figure 1.3(a) shows the payoffs in dollars. To play dove is to make a contribution. To play hawk is to attempt to free ride by contributing nothing. Thus, if Adam and Eve both play dove, each will gain 3−2 = 1 dollar, since they will then share the cost of providing the public good. If Adam plays dove and Eve plays hawk, the public good is provided with Adam footing the entire bill. He therefore loses 4−3 = 1 dollar. Eve enjoys the benefit of the public good without contributing to the cost at all. She therefore gains $3.

Since our public goods game has the structure of Figure 1.2(b), it is a version of the Prisoners’ Dilemma. As always in the Prisoners’ Dilemma, hawk strongly dominates dove, and so rational players will choose to free ride. The public good will therefore not be provided. As a result, both players will lose the extra dollar they could have made if both had volunteered to contribute.

dove hawk dove 1 3 1 −1 3 5 −1 0 5 0 hawk 3 0 1 0 (a) Prisoners’ Dilemma dove hawk dove 3 5 3 1 5 7 1 0 7 4 hawk 5 0 3 0 (b) Prisoners’ Delight

Figure 1.3 The private provision of a public good.

1.4.1 Are People Selfish?

Critics get hot under the collar about the preceding analysis. They say that game theorists go wrong in assuming that people care only about money. Real people care about all kinds of other things. In particular, they care about other people and the community within which they live. What is more, only the kind of mean-minded, money-grubbing misfits attracted into the economics profession would imagine otherwise.

But game theory assumes nothing whatever about what people want. It says only what Adam or Eve should do if they want to maximize their payoffs. It doesn’t say that a player’s payoff is necessarily the money that finds its way into his or her pocket. Game theorists understand perfectly well that money isn’t the only thing that motivates people. We too fall in love, and we vote in elections. We even write books that will never bring in enough money to cover the cost of writing them.

Suppose, for example, that Adam and Eve are lovers who care so much about each other that they regard a dollar in the pocket of their lover as being worth twice as much as a dollar in their own pocket. The payoff table of Figure 1.3(a) then no longer applies since this was constructed on the assumption that the players care only about the dollars in their own pockets. However, we can easily adapt the table to the case in which Adam and Eve are lovers. Simply add twice the opponent’s payoff to each payoff in the table. We then obtain the payoff table of Figure 1.3(b).

The new game might be called the Prisoners’ Delight because dove now strongly dominates hawk. The same principle that says that players should free ride in the Prisoners’ Dilemma therefore demands that Adam and Eve should volunteer to contribute in the Prisoners’ Delight.

Critics who think that human beings are basically altruistic therefore go astray when they accuse game theorists of using the wrong analysis of the Prisoners’ Dilemma. They ought to be accusing us of having correctly analyzed the wrong game. In the case of the private provision of public goods, the evidence would seem to suggest that they would then sometimes be right and sometimes be wrong. This is fine with game theorists, who have no particular attachment to one game over another. You tell us what you think the right game is, and we’ll do our best to tell you how it should be played.

Reason Is the Slave of the Passions. This is the famous phrase used by David Hume when explaining that rationality is about means rather than ends. As he said, there would be nothing irrational about his preferring the destruction of the entire universe to scratching his finger.

Game theory operates on the same premise. It is completely neutral about what motivates people. Just as arithmetic tells you how to add 2 and 3 without asking why you need to know the answer, so game theory tells you how to get what you want without asking why you want it. Making moral judgements—for or against—is essential in a civilized society, but you have to wear your ethical hat and not your game theory hat when doing it.

So game theory doesn’t assume that players are necessarily selfish. Even when Adam and Eve are modeled as money grubbers, who is to say why they want the money? Perhaps they plan to relieve the hardship of the poor and needy. But it is a sad fact that most people are willing to contribute only a tiny share of their income to the private provision of public goods. Numerous experiments confirm that nine out of ten laboratory subjects end up free riding once they have played a game like the Prisoners’ Dilemma with large enough dollar payoffs sufficiently often to get the hang of it. Even totally inexperienced subjects free ride half the time.

Governments are therefore wise to think more in terms of the Prisoners’ Dilemma than the Prisoners’ Delight when legislating tax enforcement measures. Nobody likes this fact about human nature. But we won’t change human nature by calling economists mean-minded, money-grubbing misfits when they tell us things we wish weren’t true.

1.4.2 Revealed Preference

The payoffs in a game needn’t correspond to objective yardsticks like money or years spent in jail. They may also reflect a player’s subjective states of mind. Chapter 4 is devoted to an account of the modern theory of utility, which justifies the manner in which economists use numerical payoffs for this purpose. This section offers a preview of the basic idea behind the theory.

Happiness? In the early nineteenth century, Jeremy Bentham and John Stuart Mill used the word utility to signify some notional measure of happiness. Perhaps they thought some kind of metering device might eventually be wired into a brain that would show how many utils of pleasure or pain a person was experiencing. Critics of modern utility theory usually imagine that economists still hold fast to some such primitive belief about the way our minds work, but orthodox economists gave up trying to be psychologists a long time ago. Far from maintaining that our brains are little machines for generating utility, the modern theory of utility makes a virtue of assuming nothing whatever about what causes our behavior.

This doesn’t mean that economists believe that our thought processes have nothing to do with our behavior. We know perfectly well that human beings are motivated by all kinds of considerations. Some people are clever, and others are stupid. Some care only about money. Others just want to stay out of jail. There are even saintly people who would sell the shirt off their back rather than see a baby cry. We accept that people are infinitely various, but we succeed in accommodating their infinite variety within a single theory by denying ourselves the luxury of speculating about what is going on inside their heads. Instead, we pay attention only to what we see them doing.

The modern theory of utility therefore abandons any attempt to explain why Adam or Eve behave as they do. Instead of an explanatory theory, we have to be content with a descriptive theory, which can do no more than say that Adam or Eve will be acting inconsistently if they did such-and-such in the past but now plan to do so-and-so in the future.

Revealed Preference in the Prisoners’ Dilemma. Analyzing the Prisoners’ Dilemma in terms of the modern theory of utility will help to clarify how the theory works. Instead of deriving the payoffs of the game from the assumption that the players are trying to make money or stay out of jail, the data for our problem ultimately comes from the behavior of the players.

In game theory, we are usually interested in deducing how rational people will play games by observing their behavior when making decisions in one-person decision problems. In the Prisoners’ Dilemma, we therefore begin by asking what decision Adam would make if he knew in advance that Eve had chosen dove.

If Adam would choose hawk, we would write a larger payoff in the bottom-left cell of his payoff matrix than in the top-left cell. These payoffs may be identified with Adam’s utilities for the outcomes (dove, hawk) and (dove, dove), but notice that our story makes it nonsensical to say that Adam chooses the former because its utility is greater. The reverse is true. We made the utility of (dove, hawk) greater than the utility of (dove, dove) because we were told that Adam would choose the former. In opting for (dove, hawk) when (dove, dove) is available, we say that Adam reveals a preference for (dove, hawk), which we indicate by assigning it a larger utility than (dove, dove).

We next ask what decision Adam would make if he knew in advance that Eve had chosen hawk. If Adam again chooses hawk, we write a larger payoff in the bottom-right cell of his payoff matrix than in the top-right cell.

On the assumption that we know what choices Adam would make if he knew what Eve were going to do, we have written payoffs for him in Figure 1.2(b) that satisfy a > b and c > d. However, the problem in game theory is that Adam usually doesn’t know what Eve is going to do. To predict what he will do in a game, we need to assume that he is sufficiently rational that the choices he makes in a game are consistent with the choices he makes when solving simple one-person decision problems.

An example will help us here. Professor Selten is a famous game theorist with an even more famous umbrella. He always carries it on rainy days, and he always carries it on sunny days. But will he carry it tomorrow? If his behavior in the future is consistent with his behavior in the past, then obviously he will. The fact that we don’t know whether tomorrow will be rainy or sunny is neither here nor there. Our data says that this information is irrelevant to Professor Selten’s behavior.

To predict Adam’s behavior in the Prisoners’ Dilemma, we need to appeal to this Umbrella Principle. Our data says that Adam will choose hawk if he learns that Eve is to play dove and that he will also choose hawk if he learns that she is to play hawk. He thereby reveals that his choice doesn’t depend on what he knows about Eve’s choice. If he is consistent, he will therefore play hawk whatever he guesses Eve’s choice will be. In other words, a consistent player must choose a strongly dominant strategy.

Criticism. Critics respond in two ways to this line of reasoning. The first objection denies the premises of the argument. People say that Adam wouldn’t choose hawk if he knew that Eve were going to choose dove. Perhaps he wouldn’t—but then we wouldn’t be analyzing the Prisoners’ Dilemma.

The second objection always puzzles me. The Prisoners’ Dilemma is first explained to the critic using some simple story that deduces the players’ behavior from the assumption that they are trying to maximize money or to minimize years spent in jail. This allows the mechanism that deduces their payoffs from their behavior in one-person decision problems to be short-circuited. When the critic objects that real people aren’t necessarily selfish, he is introduced to the theory of revealed preference and so learns that the logic of the Prisoners’ Dilemma applies to everybody, no matter how they are motivated.

Sometimes the attempt to communicate breaks down at this point because the critic can’t grasp the idea of revealed preference. Philosophers find the idea particularly troublesome because they have been brought up on a diet of Bentham and Mill. But when critics do follow the argument, a common response is to argue that, if an appeal is to be made to the theory of revealed preference, then nobody need pay attention because the result has been reduced to a tautology. They thereby contrive to reject the argument on the grounds that it is too simple to be wrong!

## 1.5 Imperfect Competition

The Mad Hatter who has just appeared in the margin is rushing onto Section 1.6 to avoid learning what relevance the Prisoners’ Dilemma has for the economics of imperfect competition. However, he will miss out on a lot if he always skips applications of game theory to economics.

It shouldn’t be surprising that game theory has found ready application in economics. The dismal science is supposedly about the allocation of scarce resources. If resources are scarce, it is because more people want them than can have them. Such a scenario creates all the necessary ingredients for a game. Moreover, neoclassical economists proceed on the assumption that people will act rationally in this game. Neoclassical economics is therefore essentially a branch of game theory. Economists who don’t realize this are like M. Jourdain in Molière’s Le Bourgeois Gentilhomme, who was astonished to learn that he had been speaking prose all his life without knowing it.

Although economists have always been close to game theorists, their progress was hampered by the fact that they didn’t have access to the tools provided by Von Neumann and Morgenstern when they invented modern game theory in 1944. As a consequence, they could offer only a satisfactory analysis of imperfect competition in the special case of monopoly. A monopoly raises no strategic questions because it can be modeled as a game with only one player. Only with the advent of game theory did it become possible to study other kinds of imperfect competition in a systematic way.

Before looking at how the Prisoners’ Dilemma can be used to illustrate a simple problem in imperfect competition, it will be helpful to see how a straightforward monopoly would work under the same circumstances.

1.5.1 Monopoly in Wonderland

The hatters of Wonderland make top hats from cardboard. Since the hatters are mad, they give their labor for free, and so the production function therefore only recognizes cardboard as an input in the hat-making process. It exhibits decreasing returns to scale because hatters are wasteful when hurried. The precise production function to be used is defined by the equation: √a = r.

This means that r sheets of cardboard will make a = r^2 top hats. Only one sheet of cardboard is therefore needed to make one top hat, but four sheets of cardboard are needed to make two top hats.

Alice is a monopolist in the hat business. Cardboard can be bought at one dollar a sheet, and so it costs her one dollar to make one top hat and four dollars to make two top hats. In general, the cost of making a top hats is given by the cost function c(a) = a^2.

If Alice can sell top hats at a price of p dollars each, her profit p is the revenue pa she derives from selling a hats minus the cost c(a) of making them: p = pa - a^2.

To know what price maximizes her profit, Alice needs to know the number a of hats that will be bought at each possible price p. In Wonderland, this information is given by the demand equation: pa = 30.

Since Alice is the only maker of hats, she can meet all the demand at any price. If she makes a hats, she will therefore be able to sell all the hats for p = 30/a dollars each. Writing this value of p into the expression for p, we find that her profit will be p = 30 - a^2.

This equation illustrates how monopolists make money. They force the price up by artificially restricting supply. In Wonderland, the effect is extreme. However many hats she sells, Alice’s revenue is always pa = $30. So she does best to reduce her cost of a^2 by making as few hats as possible. She therefore makes just one hat, which sells for $30. Since one hat costs only $1 to make, her profit is then $29.

1.5.2 Duopoly in Wonderland

A classic monopolist is a price maker, because she has complete control over the price at which her product is sold. The traders in a perfectly competitive market are price takers, because they have no control at all over the market price of the goods they trade. This is usually because all the traders are so small that any action by an individual has a negligible effect on the market as a whole. Most real markets lie between these two extremes. The traders have some partial control over the price at which goods are sold, but their control is limited by competition from their rivals.

A simple example arises when Bob decides to enter the Wonderland hat-making business as a rival to Alice. The market that then arises is called a duopoly because it has two competing producers. If Alice produces a hats and Bob produces b hats, each hat will sell for p = 30/(a + b) dollars. If Alice and Bob both care only about maximizing their own profit, how many top hats should each produce?

To keep things simple, assume that Alice and Bob are each restricted to producing either one or two hats. We can then represent their problem as a game in which each player has two strategies called dove and hawk. The payoff table of the game is shown in Figure 1.4(a). It is yet another example of the Prisoners’ Dilemma.

In a duopoly, Alice and Bob can jointly make more money by getting together to restrict supply like a monopolist. If they both play dove and so supply a total of only two top hats, each will then make a profit of $14. However, neither player will then be maximizing his or her own individual profit. In the Prisoners’ Dilemma, hawk always strongly dominates dove. No matter how many hats Alice is planning to produce, it is therefore always best for Bob to play hawk by making two hats on his own. Since the same goes for Alice, both will therefore play hawk, and the result will be that each obtains a payoff of only $11.

The outcome illustrates why competition is good for consumers. Bringing in Bob to compete with Alice raises the number of top hats produced from one to four. Simultaneously, the price of a hat goes down from $30 to $7.50. If game theory’s critics were right in saying that dove is the rational strategy for Alice and Bob in the Prisoners’ Dilemma, only two hats would be produced, and they would be sold for $15 each. It is therefore not always such a bad thing that rationality demands the play of hawk in the Prisoners’ Dilemma!

## 1.6 Nash Equilibrium

Duopolies don’t always give rise to the Prisoners’ Dilemma. Consider, for example, the effect of decreasing the demand for top hats in Wonderland so that the demand equation becomes p(a + b) = 12. We are then led to the payoff table of Figure 1.4(b). This is another example of the Prisoners’ Delight, in which dove strongly dominates hawk.

合作博弈最终导致玩家共同从消费者身上榨取最大金额。

囚徒困境与囚徒之乐可以通过剔除强占优策略来解决，但我们无法用这种方法解决所有博弈。要理解原因，请考虑爱丽丝和鲍勃的生产成本均为零且需求方程为p(a+b)²=72的情况。由此得到图1.4(c)的支付表。这个玩具博弈被称为“猎鹿博弈”，源自哲学家让-雅克·卢梭讲述的关于信任如何运作的故事。和大多数博弈一样，它没有强占优策略。如果亚当认为夏娃会选“鸽子”，他就该选“鸽子”；如果他认为她会选“老鹰”，他就该选“老鹰”。

在没有强占优策略的博弈中，理性玩法由什么决定？这个问题将我们带回奥古斯丁·古诺在不完全竞争理论起源时的思考。在提出我们一直研究的双寡头模型后，他面临同样的问题。他的答案是：我们必须寻找处于均衡中的策略。

当大卫·休谟在1739年首次提出均衡概念时，世界尚未准备好接受它。1838年古诺为该概念奠定形式基础时，世界仍未准备好。直到1944年冯·诺依曼和摩根斯特恩的《博弈论与经济行为》问世，土壤才变得肥沃。约翰·纳什在1951年重新提出古诺思想的简化版本后，该思想像野火一样迅速传播。古诺的贡献有时被认可为“古诺-纳什均衡”，但通常的做法是直接称之为“纳什均衡”。

和许多重要思想一样，解释纳什均衡几乎简单到荒谬：

一个策略对是博弈的纳什均衡，当且仅当每个策略都是对另一个策略的最佳回应。

我们已经看到许多纳什均衡。每当支付表中某个单元格的两个支付值都被圈出或框出时，我们看到的就是一个纳什均衡。

例如，在囚徒困境中，（老鹰，老鹰）总是纳什均衡，包括用于模拟简单古诺双寡头的图1.4(a)版本。同样，（鸽子，鸽子）是图1.4(b)所示囚徒之乐中的纳什均衡。在猎鹿博弈支付表（图1.4(c)）中，左上角和右下角单元格的支付值都被圈出或框出。因此，（鸽子，鸽子）和（老鹰，老鹰）都是猎鹿博弈中的纳什均衡。

为什么是纳什均衡？为什么要在意纳什均衡？至少有两个原因。第一，博弈论书籍无法权威地指出某策略对（s,t）是博弈的解，除非它是纳什均衡。例如，假设t不是对s的最佳回应。夏娃会推断：如果亚当听从书本建议选择s，那么她选择t就不会更好。但如果理性的人不按书本预测行事，书本就无法对理性行为保持权威。

进化提供了我们在意纳什均衡的第二个原因。如果博弈中的支付对应玩家的适应度，那么有利于更适应者的调整过程在达到纳什均衡时会停止运作，因为所有幸存者在当前环境下都达到了可能的最高适应度。

因此，我们的玩家不需要是数学天才，纳什均衡依然相关。它们常常能很好地预测动物行为。纳什均衡的进化意义也不仅限于生物学。每当某些调整过程倾向于淘汰获得低支付的玩家时，纳什均衡就具有预测作用。例如，表现不如竞争对手的股票经纪人会破产。股票经纪人使用的经验法则因此面临与鱼类或昆虫基因相同的进化压力。因此，尽管我们都知道有些股票经纪人连金鱼缸都找不到路，更别说博弈论书籍，但考察股票经纪人所玩博弈的纳什均衡仍然有意义。

1.6.1 自私的基因？

因为当达到纳什均衡时进化停止运作，生物学家称纳什均衡是进化稳定的。染色体上每个相关位点都被具有最大适应度的基因占据。由于基因只是分子，它无法选择最大化自己的适应度，但进化使其看起来仿佛在这样做。因此，博弈论让生物学家无需追踪进化过程的每一步转折，就能把握进化过程的最终结果。

理查德·道金斯著名作品《自私的基因》的标题简洁表达了这一思想。他的比喻生动但有风险。我特别喜欢看一位老妇人斥责他胆敢宣扬这种进化谬论——我们都能看到基因只是分子，因此不可能有自由意志。

1.6.2 血浓于水

遗憾的是篇幅不允许对博弈论的生物学应用进行充分讨论，但仍有时间思考比尔·汉密尔顿的解释：为什么我们预期动物（和人类）与亲属相处比与陌生人更融洽。

大致而言，一个基因的适应度是其在下一代中出现的平均拷贝数。然而，如果爱丽丝体内的一个基因在计算适应度时忽略了其拷贝可能已存在于爱丽丝亲属体内的概率，那它就是疏忽的。毕竟，如果爱丽丝的兄弟携带该基因，他平均为下一代贡献的基因拷贝数将与爱丽丝本人一样多。

爱丽丝与鲍勃之间的亲缘关系度r是他们共享任何特定基因的概率。如果鲍勃是爱丽丝的全兄弟，则r=1。如果他们是全表亲，则r=1/4。如果爱丽丝和鲍勃彼此对弈，比如像巢中的雏鸟那样，r会如何影响结果？

我们仅考虑r=1的情况，即爱丽丝和鲍勃是同卵双胞胎或克隆体。如果他们在囚徒困境中的策略由占据特定位点的基因决定，该基因知道决定对手策略的正是自身的拷贝（练习1.13.26）。因此实际上只有一个基因在参与博弈。在这个单人博弈中，最优选择是鸽子，因此爱丽丝和鲍勃会合作。简而言之，双胞胎悖论不再成立，因为爱丽丝和鲍勃确实是彼此的精确复制品。

如果爱丽丝和鲍勃亲缘关系较远，则适用1.4.1节中恋人故事的修改版本。r越大，他们越可能合作（练习1.13.29）。汉密尔顿指出，这必定是膜翅目昆虫（蚂蚁、蜜蜂和黄蜂）中社会性独立进化多次的原因。由于其特殊的繁殖方式，该物种中两姐妹的r=2，而我们人类r=1。

## 1.7 集体理性？

冯·诺依曼和摩根斯特恩的《博弈论与经济行为》区分了两种博弈理论。到目前为止，我们只讨论了非合作博弈，其中玩家独立选择策略以最大化自身支付。对囚徒困境的博弈论分析的批评者有时会质问，为何我们反常地选择忽略冯·诺依曼和摩根斯特恩的合作博弈理论——该理论假设玩家在博弈开始前通过谈判就使用何种策略达成有约束力的协议。此类批评者通常信奉理性存在于群体而非个体的观念。因此他们认为个体玩家的理性行为仅在于同意对整个玩家群体来说合理的事情。卡尔·马克思是这一错误最著名的倡导者。该错误的生物学版本被称为群体选择谬误。

帕累托效率。合作博弈理论的一个标准假设是理性协议将是帕累托有效的。帕累托有效有弱形式和强形式。弱形式最容易辩护，它指出当不存在所有玩家都偏好的其他可行协议时，该协议是帕累托有效的。假设协议将是弱帕累托有效的理由在于，只要继续谈判能让所有人获益，理性玩家就不会停止谈判。然而，囚徒困境四种结果中唯一非帕累托有效的是（老鹰，老鹰），而这恰恰是非合作博弈理论预测理性玩法将导致的结果。

认为这一事实揭示了非合作与合作博弈理论之间矛盾的哲学家，忽略了合作博弈理论中可达成有约束力协议这一假设的重要性。仅凭亚当和夏娃承诺遵守协议是不够的。我们都曾在某个时刻违背诺言，因为当时似乎有其他事情更重要。对于真正有约束力的协议，所有玩家必须知道每个人在需要时都有压倒性的理由信守承诺。博弈论学者称此时玩家知道他们都致力于遵守协议。

让承诺有效。在现实生活中，我们的法律系统通常提供了执行承诺的可行方式。如果亚当和夏娃各自签署具有法律约束力的合同，那么当违约惩罚超过作弊带来的任何优势时，他们将有效地致力于这笔交易。然而，将此类达成承诺的机会构建到模型中不可避免地改变了所玩博弈，从而消除了批评者认为他们看到的矛盾。

例如，假设亚当和夏娃在囚徒困境博弈开始前讨论并同意双方都选择鸽子。我们可以将他们的两个策略重新标记为“信守承诺选择鸽子”和“违背诺言选择老鹰”。如果该协议具有法律约束力，那么两位玩家若违约都将承担法律责任。

k their word. Figure 1.5(a) shows how a penalty of three dollars for breaching the contract changes the Prisoners’ Dilemma used to model the private provision of public goods in Figure 1.3(a). The new game is another version of the Prisoners’ Delight of Figure 1.3(b), in which dove strongly dominates hawk. Keeping your word therefore becomes the rational strategy, and so each player’s promise to play dove is effectively a commitment.

Modeling Promises. People who think that game theory is immoral sometimes downplay the need for external enforcement by arguing that a player’s conscience serves as an internal policeman. Game theorists have no difficulty in modeling the fact that most people don’t like breaking promises. But how bad does breaking a promise make you feel? I wouldn’t feel at all bad about breaking a promise if there were no other way to get money to feed my starving child. Some people feel the same about all promises—otherwise we wouldn’t need to bother with a legal system at all. We therefore need to face up to the fact that the amount that needs to be subtracted from my payoff to capture my distress at breaking a promise may be too small to affect my behavior.

As an example, consider again the Prisoners’ Dilemma of Figure 1.3(a) used to model the private provision of public goods. If we only subtract fifty cents from Eve’s payoff when she breaks her promise to play dove but continue to subtract three dollars from Adam’s payoff when he breaks his promise, then we are led to the game of Figure 1.5(b). This is the first asymmetric game we have encountered, but we can still solve it by eliminating strongly dominated strategies. It is rational for Adam to play dove and Eve to play hawk.

Eve therefore free rides while Adam pays the full cost of providing the public good. But Adam isn’t the classic sucker who is never to be given an even break. He predicts that Eve is going to play hawk but plays dove anyway because he values his peace of mind more than the money he would save by playing hawk. If this weren’t the case, the theory of revealed preference tells us that three dollars would have been too large a penalty to write into his payoffs.

1.7.1 Collusion People often react badly to the suggestion that it may be rational to cheat and lie. They think that society would collapse if such things were true. Where would we be if we couldn’t trust our friends and neighbors? But game theorists don’t say that rational people should never trust each other. They only say that it is irrational to do something without being able to give a good reason for doing it.

We have good reasons for trusting our friends and neighbors, but we have equally good reasons for distrusting politicians and used-car salesmen. Whether it is sensible to put our trust in other people depends on the circumstances. For example, everybody knows not to trust a stranger who approaches you in a dark alley late at night.

Game theorists argue that it would be unwise for Adam to trust Eve’s word if they were about to play the Prisoners’ Dilemma. He should get her signature on a legally binding contract before counting on her cooperation. However, if Eve were Adam’s wife or sister, they wouldn’t be playing the Prisoners’ Dilemma. The games we play with those we trust are much more complicated.

An important assumption built into the Prisoners’ Dilemma is that the players will never interact again. If Adam and Eve believed they might meet in the future to play again, they would have to take into account the impact that their choice of dove or hawk in the present might have on the choices their opponent might make in the future. The Prisoners’ Dilemma is therefore not capable of modeling long-term relationships in which a player’s reputation for honesty can be very valuable—and easily lost. As a dealer in curios put it in the New York Times of 29 August 1991 when asked whether he could rely on the honesty of the owner of the antique store that sold his goods on commission: ‘‘Sure I trust him. You know the ones to trust in this business. The ones who betray you, bye-bye.’’

A duopoly is a good setting within which to consider the problem of trust because cooperation among duopolists is commonly illegal. We even use a special word to register our disapproval. When two duopolists agree to cooperate rather than compete, we say that they are colluding.

Collusion in a duopoly can’t be sustained legally because neither party is going to sue the other for failing to honor a contract that it would be illegal to sign. Nor is it hard to imagine that colluding duopolists will lack moral scruple. After all, it is hardly compatible with an upright nature to enter into a conspiracy whose aim is to screw the consumer. Indeed, in real life, colluding executives seem to relish their shady dealing by choosing to meet in smoke-filled hotel rooms late at night—just like gangsters in the movies.

If Alice and Bob are to collude successfully, they therefore need to have a good reason to trust each other, even though each knows that the other is motivated only by a selfish desire to maximize his or her own profit. A proper explanation of how cooperation can be sustained in an ongoing relationship without internal or external enforcement will have to wait until we study the theory of repeated games (Section 11.3.3). However, it is easy to give the flavor of the explanation while correcting yet another fallacious line of reasoning that has been proposed by philosophers.

The Transparent Disposition Fallacy. The transparent disposition fallacy asks us to believe two doubtful propositions. The first is that rational people have the willpower to commit themselves in advance to playing games in a particular way. The second is that other people can read our body language well enough to know when we are telling the truth. If we truthfully claim that we have made a commitment, we will therefore be believed.

If these propositions were correct, our world would certainly be very different! Rationality would be a defense against drug addiction. Poker would be impossible to play. Actors would be out of a job. Politicians would be incorruptible. However, the logic of game theory would still apply.

As an example, consider two possible mental dispositions called clint and john. The former is named after the character played by Clint Eastwood in the spaghetti westerns. The latter commemorates a hilarious movie I once saw in which John Wayne played the part of Genghis Khan. To choose the disposition john is to advertise that you have committed yourself to play hawk in the Prisoners’ Dilemma no matter what. To choose the disposition clint is to advertise that you are committed to playing dove in the Prisoners’ Dilemma if and only if your opponent is advertising the same commitment. Otherwise you will play hawk.

If Alice and Bob are allowed to commit themselves transparently to one of these two dispositions before playing the Prisoners’ Dilemma of Figure 1.4(a), what should they do? Their problem is a game in which each player has two strategies, clint and john. The outcome of this Film Star Game is (hawk, hawk) unless both players choose clint, in which case it is (dove, dove). The payoff table for their game is therefore given by Figure 1.6(a).

The Film Star Game has no strongly dominant strategies. It is always a best reply for Alice to choose clint, but clint isn’t always her only best reply. If Alice predicts that Bob will choose john, then she gets the same payoff whether she chooses clint or john. Under such circumstances, we say that clint weakly dominates john.

A rational player must play hawk in the Prisoners’ Dilemma because hawk strongly dominates dove. We can’t say that rational players must play clint in the Film Star Game because it is also a Nash equilibrium for both to play john. However, if Alice or Bob entertains any doubt at all about which strategy the other will choose, he or she does best to play clint because clint is sure to be a best reply, whereas john is only a best reply if the other player also chooses john.

If Alice and Bob can successfully advertise having made a commitment to play like clint, then both will play dove in the Prisoners’ Dilemma. Advocates of the transparent disposition fallacy think that this shows that cooperation is rational in the Prisoners’ Dilemma. It would be nice if they were right in thinking that real-life games are really all film star games of some kind—especially if one could choose to be Adam Smith or Charles Darwin rather than John Wayne or Clint Eastwood. But even then they wouldn’t have shown that it is rational to cooperate in the Prisoners’ Dilemma. Their argument shows only that it is rational to play clint in the Film Star Game.

## 1.8 Repeating the Prisoners’ Dilemma

If rational cooperation is impossible in the Prisoners’ Dilemma, how come duopolists like Alice and Bob often succeed in colluding in real life? The reason is that the real world is more complicated than Wonderland. Real duopolists don’t make their decisions once and for all but compete on a day-by-day basis. The Prisoners’ Dilemma doesn’t capture the essence of such ongoing economic interaction, but we can create a toy game that does by supposing that Alice and Bob must play the Prisoners’ Dilemma every day from now until eternity. Their payoffs in this new game are simply their average daily profits.

When we study repeated games seriously, we will find that Alice and Bob have huge numbers of strategies, but we will just look at three: dove, hawk, and grim. The first of these is the strategy of always playing dove. The second is the strategy of always playing hawk. The third is the strategy of playing dove as long as your opponent does the same, but switching permanently to hawk the day after your opponent first fails to reciprocate.10

If our only strategies were dove and hawk, the repeated Prisoners’ Dilemma would be the same as the one-shot version, but we also have grim to worry about. When grim plays dove or itself, both players use dove every day, and so each gets a daily payoff of fourteen dollars. Things get complicated only when grim plays hawk. The first day will then see one player using dove and the other hawk. On all subsequent days, bo th players will use hawk because grim requires that a failure to reciprocate its play of dove on the first day be punished forever. If one player uses grim and the other hawk, each therefore gets an average payoff of 11 because the payoffs Alice and Bob get on the first day are irrelevant when computing averages over an infinite period.

Putting these facts together, we are led to the payoff table of Figure 1.6(b), which is only a tiny part of the true payoff table of the repeated Prisoners’ Dilemma, because we have considered only three of the vast number of possible strategies. If we didn’t have grim in the table, we would be back with the one-shot Prisoners’ Dilemma. If we didn’t have dove, we would be back with the Film Star Game. This perhaps explains why philosophers are so enthusiastic about Clint. They have seen Clint Eastwood playing a version of the grim strategy in the spaghetti westerns, but they didn’t notice that he tries to get along with the bad guys before reaching for his gun and that the bad guys totally fail to read the body language with which he conveys his talents as a gunslinger.

Two of the cells of the payoff table of Figure 1.6(b) have both their payoffs enclosed in a circle or a square. These correspond to two Nash equilibria. We are familiar with the equilibrium in which both players use hawk. But this is now joined by a new equilibrium in which Alice and Bob both use grim and hence collude by playing dove in each repetition of the Prisoners’ Dilemma. They thereby squeeze the maximum possible amount out of the consumer.

The grim equilibrium shows how collusion can survive in a duopoly. Alice and Bob need neither a legal system nor a sense of moral obligation to keep them from cheating if they agree to operate a Nash equilibrium. In the case of the grim equilibrium, a player who cheats on the agreement will simply provoke the other player into switching to hawk on all subsequent days. Neither player therefore has an incentive to cheat.

Sometimes this result is trumpeted as the “solution” to the paradox of rationality raised by the Prisoners’ Dilemma. It is certainly important for game theory that we have found a Pareto-efficient Nash equilibrium in the repeated Prisoners’ Dilemma. We can thereby explain how cooperation can survive in long-term relationships without the need for external enforcement. But only confusion can result from confounding the repeated Prisoners’ Dilemma with the Prisoners’ Dilemma itself. The only Nash equilibrium in the one-shot Prisoners’ Dilemma continues to require that both players use hawk.

The grim strategy gets its name because it punishes an opponent’s transgression relentlessly. Many readers will have heard of the strategy tit-for-tat. Popular writers are mistaken when they assert that this strategy outperforms all rivals.

## 1.9 Which Equilibrium?

We found two Nash equilibria in both the Stag Hunt Game and the simplified repeated Prisoners’ Dilemma of Figure 1.6. The full repeated Prisoners’ Dilemma has an infinite number of Nash equilibria. We therefore have to confront what game theorists call the equilibrium selection problem. Which equilibrium should we choose?

No attempt will be made to answer this question here, except to say that nothing says that there must be a “right” equilibrium. After all, nobody thinks there has to be a “right” solution to a quadratic equation. We choose whichever solution fits the problem from which the quadratic equation arose. So why should things be different in game theory?

Advocates of collective rationality don’t like this answer. They say that rationality demands the choice of a Pareto-efficient equilibrium in those cases where one exists. But the Stag Hunt Game of Figure 1.4(c) should give them pause. Under the name of the Security Dilemma, experts in international relations use this game to draw attention to the limitations of rational diplomacy.

In the Stag Hunt Game, the Nash equilibrium in which both Alice and Bob play dove is Pareto efficient. But suppose their game theory book says that hawk should be played. Could rational players persuade each other that the book is recommending the wrong equilibrium? Alice may say that she thinks the book is wrong, but would Bob believe her?

Whatever Alice is planning to play, it is in her interests to persuade Bob to play dove. If she succeeds, she will get 18 rather than 8 when playing dove, and 16 rather than 9 when playing hawk. Rationality alone therefore doesn’t allow Bob to deduce anything about her plan of action from what she says because she is going to say the same thing no matter what her real plan may be! Alice may actually think that Bob is unlikely to be persuaded to switch from hawk and hence be planning to play hawk herself, yet still try to persuade him to play dove.

The point of this Machiavellian story is that attributing rationality to the players isn’t enough to resolve the equilibrium selection problem—even in a case that seems as transparently straightforward as the Stag Hunt Game. If we see Alice and Bob playing hawk in the Stag Hunt Game, we may regret their failure to coordinate on playing dove, but we can’t accuse them of being irrational because neither player can do any better, given the behavior of their opponent (Section 12.9.1).

## 1.10 Social Dilemmas

Psychologists refer to multiplayer versions of the Prisoners’ Dilemma as social dilemmas. You can usually tell that you are in a social dilemma by the fact that your mother would register her disapproval of any hawkish inclination on your part by saying, “Suppose everybody behaved like that?”

Immanuel Kant is sometimes said to be the greatest philosopher of all time, but he too thought that it couldn’t be rational to do something if it would be bad if everybody did it. As his famous categorical imperative says:

Act only on the maxim that you would will to be a universal law.

For example, when waiting at an airport carousel for our bags, we would all be better off if we all stood well back so that we could see our bags coming. The same applies when people stand up at a football match or when they conduct their business in slow motion after reaching the head of a long line.

When large numbers of anonymous folk play such social dilemmas, Kant and your mother are right to predict that things will work out badly if everybody behaves antisocially. But urging people to behave better in such situations is seldom very effective. Why should you lose out by paying heed to your mother when everybody else is ignoring theirs?

1.10.1 Tragedy of the Commons

The kind of everyday social dilemma just described can be irritating, but some social dilemmas spell life or death for those who are forced to play them. The standard example is called the Tragedy of the Commons in the political science literature. If you can follow the calculus needed to explain this game properly, you probably know enough mathematics to get started on this book. The Mad Hatter in the margin is there to suggest that readers who find the mathematics challenging would nevertheless be wise not to skip the material.

Ten families herd goats that graze on one square mile of common land. The milk a goat gives per day depends on how much grass it gets to eat. A goat that grazes on a fraction a of the available common land produces

b = e^(1 - 1/10a)

buckets of milk a day. This production function has been chosen so that a goat that grazes on one-tenth of the common land gives one bucket of milk. As the fraction of land available for it to graze decreases, the goat’s yield progressively declines until a goat without grass to eat gives no milk at all.

A social planner asked to decide the optimal total number N of goats would first note that each goat would occupy a fraction a = 1/N of the common land. Total milk production is then

M = Nb = Ne^(1 - N/10),

which is largest when N = 10, making total milk production M = 10 buckets a day. If all families are to share equally in the milk produced, the planner would therefore assign the ten families one goat each. Each family would end up with one-tenth of the total milk production, which is one bucket a day per family.

But suppose the planner’s edicts can’t be enforced. Each family will then make its own decision on the number g of goats to keep. Its own milk production is

m = gb = ge^(1 - (g + G)/10) = e^(-G/10) ge^(1 - g/10),

where G is the total number of goats kept by all the other families. Since G stays constant while our family makes its decision, the solution of its maximization problem is the same as the planner’s. It will therefore keep ten goats, regardless of how many goats the other families choose to keep. Since all ten families will do exactly the same, the result will be that one hundred goats are turned loose on the common land, which will therefore be grazed into a desert. When N = 100, total milk production is

M = 100 e^(-9) = 0.012,

which is just about enough to wet the bottom of a bucket.

Figure 1.7 makes the connection with the Prisoners’ Dilemma in a variety of ways. Figure 1.7(a) substitutes for a player’s payoff matrix. It shows a family’s milk production as a function of the number g of goats that it keeps and the total number G of goats kept by all the other families. Figure 1.7(b) shows the same data in the form of a contour map. The graphs of Figure 1.7(c) are slices through the milk-production surface of Figure 1.7(a), in which g is held constant. One can think of such slices as representing rows in the payoff matrix. Figure 1.7(d) shows slices through the milk-production surface in which G is held constant. One can think of such slices as columns in the payoff matrix.

A strategy for a family in the Tragedy of the Commons is the number g of goats that it chooses to keep. These strategies are represented as graphs in Figure 1.7(c), or as points on the horizontal axis in Figure 1.7(d). It is easier to see that the hawkish strategy of keeping ten goats is strongly dominant in Figure 1.7(c). One only has to take note of the fact that the graph corresponding to g = 10 always lies above each of the graphs corresponding to other strategies. Whatever the value of G, a family therefore always gets more milk by keeping ten goats than by keeping any other number of goats. In particular, the hawkish strategy of keeping ten goats strongly dominates the dovelike strategy advocated by the planner of keeping one goat.

gonlyonegoat.

Nevertheless, everybody would be far better off if everybody had taken the planner’s advice.

The Tragedy of the Commons captures the logic of a whole spectrum of environmental disasters that we have brought upon ourselves. The Sahara Desert is relentlessly expanding southward, partly because the pastoral peoples who live on its borders persistently overgraze its marginal grasslands. But the developed nations play the Tragedy of the Commons no less determinedly. We jam our roads with cars. We poison our rivers and pollute the atmosphere. We fell the rainforests. We have plundered our fishing areas until some fish stocks have reached a level from which they may never recover.

What is to be done about the Tragedy of the Commons? Nobody likes where the logic of the game theory argument leads, but it doesn’t help to insist that the logic must therefore be wrong. One might as well complain that arithmetic must be wrong because seven loaves and two fishes won’t feed a multitude. Nor does there seem much point in arguing that we can rely on people caring for each other to get us out of such messes. If we could, the mess wouldn’t have arisen in the first place.

Game theorists prefer a more positive approach. When they are convinced that they have gotten the game right but don’t like the answer to which its analysis leads, they ask whether it may be possible to change the game.

1.10.2 Mechanism Design The rules of a game are sometimes called a mechanism. Mechanism design is therefore the branch of game theory in which one asks whether games can be invented that rational people will play in socially beneficial ways.

It is realistic to think of changing the game only if a government or some other powerful planning agency is able to monitor and enforce the new rules, but central planners are notorious for knowing less about what needs to be done than the people they order around. In a good design, the planner therefore doesn’t tell everybody what to do. The decisions are left to the people who have the necessary knowledge and expertise. The role left for the planner is to guide their decisions in a socially desirable direction by enforcing a carefully designed system of incentives and constraints. We can then get the logic of game theory to work for us instead of against us.

It will come as no surprise that working out the best system of incentives and constraints can often be difficult, but we can use the Tragedy of the Commons to get the general idea. We have seen that a planner who knew as much about keeping goats as a goatherder would issue each family a license to keep one goat. However, a real planner would be unlikely to know that ten licenses is the socially optimal number.

Suppose, for example, that the planner knows only that each goat’s milk production function is of the form b=e^{(1-A)/a}, but that you need to have herded goats all your life to be aware that A=10. The planner can work out that the socially optimal number of goats is A, but you can’t issue A licenses if you don’t know what A is. A stupid planner might guess at the value of A and issue that many licenses, but a clever planner will exploit the goat herders’ knowledge and experience and let them make the decision on how many goats to keep themselves.

We know that the goatherders will choose in a disastrous way unless the planner intervenes somehow. There are various ways the planner might manipulate their choice. If it is possible for the planner to confiscate the entire milk production and then divide it equally among the ten families, the outcome is particularly benign because each family’s aim then becomes the same. They no longer have an incentive to put one over on their neighbors by sneaking an extra goat onto the common. Their common goal is now to maximize the total amount of milk produced.

To be pedantic, each of the ten families forced to play the planner’s confiscation game will now choose g to maximize m = ((g+G)/10)e^{(g+G)/A}, which is largest when g+G=A. If each family makes a best reply to the strategies chosen by their opponents—so that a Nash equilibrium is played—the total number g+G of goats that graze the common land will then be socially optimal. However, the planner will find out that the socially optimal number is ten only after counting the number of goats that get turned loose on the common after the new rules are introduced.

1.10.3 Second Best It shouldn’t be thought that it is always possible for a social planner to find a way to get to the socially optimal outcome. For example, the mechanism we have just considered won’t work if the planner can’t monitor how much milk each goat produces since the goatherders have an incentive to keep back some of the milk for their own private use.

Economists express the fact that the best workable mechanism may fail to match up with what an omniscient and omnipotent planner would be able to achieve by saying that, when the first-best outcome isn’t available, we have to be satisfied with the second-best outcome.

People who insist that it must be rational to cooperate in the Prisoners’ Dilemma also reject second-best outcomes. When they insist on nothing less than the first-best, economists believe that they are denying the most elementary principle of decision theory—one must first decide what is feasible before thinking about which of the feasible alternatives is optimal.

The feasible solutions to a problem are those that will work. For example, feasible solutions to reaching a high shelf would be to stand on a chair or to use a broom to lengthen your reach. An infeasible solution would be to swallow the contents of a bottle called Drink-Me in the hope that it will make you grow taller. The optimal solution to the problem is the feasible alternative that costs you least in time and trouble. Standing on a chair is therefore probably optimal, even though putting the chair in the right place and climbing up on it will be a nuisance. However, if you emulate Alice by trying to find a bottle labeled Drink-Me, you will never reach the high shelf at all. In rejecting the second-best outcome in favor of an illusory first-best outcome, you condemn yourself to a third-best or worse outcome.

Planners are particularly likely to make this kind of error when reforming human organizations. They fail to see that people will change their behavior in response to the new incentives created by the reform.

The U.S. Congress made precisely such a mistake in 1990 when it passed an act intended to ensure that Medicare wouldn’t pay substantially more for its drugs than private health providers. The basic provision of the act said that a drug must be sold to Medicare at no more than 88% of the average selling price. The problem was created by an extra provision that said that Medicare must also be offered at least as good a price as any retailer. This provision would work as its framers intended only if drug manufacturers could be relied upon to ignore the new incentives created for them by the act. But why would drug manufacturers ever sell a drug to a retailer at less than 88% of the current average price if the consequence is that they must then sell the drug at the same price to a huge customer like Medicare? However, if no drugs are sold at less than 88% of the current average, then the average price will be forced up!

Mechanism design corrects this kind of error by using game theory to predict how people’s behavior will adapt after a reform has been implemented. Only then can we know what outcomes are genuinely feasible and so make a reasoned choice of what is optimal.

## 1.11 Roundup

Each chapter in this book ends with a summary of the material it covers. Usually, the vital definitions and results are reviewed to give a sense of what is of primary importance. This introductory chapter is exceptional in that the concepts it introduces are dealt with again more carefully in later chapters. The lessons that need to be learned from this chapter are philosophical.

Don’t despise toy games. Even a game as simple as the Prisoners’ Dilemma is the object of an ongoing controversy. The fact that rational players won’t cooperate in the Prisoners’ Dilemma isn’t a paradox of rationality. People who think this usually make the mistake of imagining that the Prisoners’ Dilemma captures the essentials of what matters about human interaction in general, but the one-shot Prisoners’ Dilemma is actually a game whose structure is exceptionally hostile to the emergence of cooperation. In games that better capture the circumstances under which people cooperate in real life, rational players won’t necessarily double-cross each other. For example, in the game created by repeating the Prisoners’ Dilemma infinitely often, we identified a Nash equilibrium in which the players always cooperate.

When critics offer rival analyses of the Prisoners’ Dilemma, they usually fail to notice that they are substituting some other game for the Prisoners’ Dilemma. They often mistakenly believe that game theory requires that people care only about how much money they have in their own pockets. They seem never to understand that the payoffs in game theory are derived in principle from the theory of revealed preference. This assumes nothing whatever about what motivates people but simply asks that people make decisions consistently. Game theory is neutral on moral and psychological issues.

The basic concept of game theory is called a Nash equilibrium. It arises when all players choose a strategy that is a best reply to the strategies chosen by the other players. It is important for two reasons. The first is that a great book of game theory that listed the “rational solutions” of all games would never list a strategy profile that isn’t a Nash equilibrium. If it did, at least one player would have an incentive to deviate from the book’s advice, and so its advice wouldn’t be authoritative. The second reason is evolutionary. An evolutionary process—economic, social, or biological—that acts to maximize the fitness of the players will cease to operate when it reaches a Nash equilibrium. Part of the success of game theory lies in the possibility of switching back and forth between the two interpretations. In particular, we can use the language of rational optimization when talking about the end product of trial-and-error processes of evolutionary adaptation.

Although human interactions that can effectively be modeled using variants of the Prisoners’ Dilemma are rare, the results can be disastrous when they do arise. The Tragedy of the Commons is a particularly sad case. In such situations, game theorists don’t bury their heads in the sand by pretending that some more amenable game is being played—they ask whether it is actually possible to change the rules to create a more amenable game.

The science of designing new games that rational people will play in a desirable way is called mechanism design. Perhaps it will one day become a routine instrument of good government. In the meantime, game theorists advocate its use wherever we understand what is going on well enough to be able to predict how people will respond to the novel incentives created by a newly designed game.

## 1.12 Further Reading

Thinking Strategically, by Barry Nalebuff and Avinash Dixit: Norton, New York, 1991. This best-selling book is written for a popular audience. It contains many examples of game theory in action, both in business and in everyday life.

Playing Fair: Game Theory and the Social Contract I, by Ken Binmore: MIT Press, Cambridge, MA, 1995. Chapter 3 discusses many fallacies of the Prisoners' Dilemma that circulate in the philosophical literature.

A Beautiful Mind, by Sylvia Nasar: Simon and Schuster, New York, 1998. Few of us will experience the highs and lows that are described in this biography of John Nash. There is now a movie with the same title.

John Von Neumann and Norbert Wiener, by Steve Heine: MIT Press, Cambridge, MA, 1982. People who knew Von Neumann say he was so clever that it was like talking to someone from another planet.

Evolution and the Theory of Games, by John Maynard Smith: Cambridge University Press, Cambridge, UK, 1982. This beautiful book introduced game theory to biology.

Behavioral Game Theory, by Colin Camerer: Princeton University Press, Princeton, NJ, 2003. Some bits of game theory work well in the laboratory, and some don't. This book surveys the evidence and looks at possible psychological explanations of deviations from the theory.

## 1.13 Exercises

1. The simplest strategic story that yields the Prisoners' Dilemma arises when Adam and Eve both have access to a pot of money. Both are independently allowed either to give their opponent $2 from the pot, or to put $1 from the pot in their own pocket. Write down the payoff table of the game on the assumption that the players care only about how many dollars they make. Which strategy is strongly dominant?

2. A feasible outcome is (weakly) Pareto efficient if there is no other feasible outcome that all the players prefer. Explain why only the outcome (hawk, hawk) isn't Pareto efficient in the Prisoners' Dilemma. What are the Pareto-efficient outcomes in the Stag Hunt Game?

3. A sealed-bid auction is to be used to sell a collection of ten old coins to the highest bidder at the price he or she bids. The only bidders are Alice and Bob, who both value each coin at $10. If both make the same bid, each pays half their bid for half the coins. Assuming they are restricted to bidding only $97 or $98, show that they are playing a Prisoners' Dilemma in which the strongly dominant strategy is to bid high. Show that the same is true if the only possible bids are $99.97 and $99.98.

4. Tenants who sweep the hallways in apartment buildings without a janitor provide a public good. Formulate a version of the Prisoners' Dilemma based on this story.

5. The classic toy game called Chicken derives from the James Dean movie Rebel without a Cause, in which two teenage boys drive cars toward a cliff edge to see who chickens out first. The same game is played by middle-aged drivers who approach each other in streets too narrow for them to pass without someone slowing down. Explain why the payoff table of Figure 1.8(a) fits both stories. Enclose the payoffs that correspond to best replies in a circle or a square. Explain why neither player has a dominant strategy. Why are (slow, speed) and (speed, slow) Nash equilibria? What are the Pareto-efficient outcomes in this game?

6. A couple on their honeymoon in New York are separated in the crowds without having agreed on where they should go in the evening. At breakfast, they had discussed either a visit to the ballet or a boxing match. Explain why the Battle of the Sexes of Figure 1.8(b) might be used to model their dilemma. Enclose the payoffs that correspond to best replies in a circle or a square. Explain why neither player has a dominant strategy. Why are (box, box) and (ball, ball) Nash equilibria? What are the Pareto-efficient outcomes in this game?

12 The sexist assumption that the row player is the husband is usually made, but my wife and I are at least one couple that the stereotype doesn't fit.

7. The favorite toy game of evolutionary biologists is called the Hawk-Dove Game. Two birds of the same species are competing for a scarce resource. Each can behave aggressively or passively. Payoffs are measured in terms of a bird's fitness—the extra number of offspring the bird will have on average as a result of the way the game was played. If one bird is aggressive and the other is passive, the aggressive bird takes the entire resource. The aggressive bird then gets a payoff of V>0, and the passive bird gets 0. If both birds are passive, the resource is shared, and each bird gets a payoff of 1V. If both birds are aggressive, there is a fight, and both birds receive a payoff of W. If 0<W< 1V, show that the Hawk-Dove Game is an example of the Prisoners' Dilemma. If the damage a bird is likely to receive in a fight is sufficiently large, then W<0. Show that the Hawk-Dove Game then reduces to a version of the game Chicken, introduced in Exercise 1.13.5.

8. Adapt Exercise 1.13.1 to obtain an asymmetric version of the Prisoners' Dilemma. Confirm that hawk is a strongly dominant strategy but that the outcome (hawk, hawk) is Pareto inefficient.

9. In Section 1.4.1, the Prisoners' Dilemma of Figure 1.3(a) was converted to the Prisoners' Delight of Figure 1.3(b) by changing the assumption that Adam and Eve care only about themselves to the assumption that they care twice as much about their partner as they do about themselves. What happens if Adam and Eve both care r times as much about their partner as they care about themselves? Show that: a. They are still playing the Prisoners' Dilemma when 0≤r< 1.

b. They are playing the Prisoners' Delight when r>1.

c. They are playing a version of Chicken when 1 <r<1.

10. Explain why neither hawk nor dove is strongly dominant when 1≤r ≤1 in the previous problem. For what values of r does the game have a weakly dominant strategy?

11. Section 1.5.1 describes Alice operating a monopoly in Wonderland. Instead of a single Alice acting as a price maker, assume that there are fifteen hat manufacturers acting as price takers. Analyze this example of perfect competition, and show that each manufacturer makes one hat, which sells for $2. What is the total profit of the manufacturers? How does this compare with Alice's profit?

12. In Section 1.5.2, the sum of the profits of the duopolists who make one hat each is $28. A monopolist who made two hats would obtain a profit of only $26. Trace this apparent anomaly to the fact that the production function has decreasing returns to scale.

13. Discuss monopoly and duopoly in the example of Section 1.5 when the production function is a¼r2, which has increasing returns to scale. Why is it problematic to attempt an analysis of perfect competition along the lines of Exercise 1.13.11?

14. Section 1.5.2 derives the Prisoners' Dilemma from a problem in which Alice and Bob compete in a market with demand equation p(aþb)¼X. Show that the Prisoners' Dilemma arises when X>18, and the Prisoners' Delight when X<18. What happens when X¼18?

## 15. Why can the following situations be thought of as social dilemmas?

a. Everybody talking louder and louder in a restaurant until nobody can hear what anybody is saying.

b. Watering your garden in a drought.

c. Sneaking excess hand baggage onto a crowded airplane. Think of at least one more everyday example.

16. Suppose that the milk production function in the Tragedy of the Commons takes the form given in Section 1.10.2. Verify that the socially optimal number of goats is A.

17. Each of n farmers can costlessly produce as much wheat as he or she chooses. If the total amount of wheat produced is W, the price at which wheat sells is determined by the demand equation p¼e(cid:1)W.

a. Show that the strategy of producing one unit of wheat strongly dominates all of a profit-maximizing farmer's other strategies. Verify that the use of this strategy yields a profit of e(cid:1)n for a farmer.

b. Explain why the best agreement that treats each farmer equally requires each to produce only 1=n units of wheat. Verify that a farmer's profit is then 1=en. Why would such an agreement need to be binding for it to be honored by profit-maximizing farmers?

c. Confirm that xe(cid:1)x is largest when x¼1. Deduce that all the farmers would make a larger profit if they all honored the agreement rather than each producing one unit and so flooding the market.

This problem has the same structure as the Tragedy of the Commons of Section 1.10.1, but the consumers are unlikely to regard it as tragic if the farmers are unable to agree to restrict their production to 1=n units of wheat. What term will the consumers use to describe the farmers' agreement if they succeed in making it stick?

18. Political scientists regard the following "wasted vote" problem as a relative of the Tragedy of the Commons. Of 100 people who live in a village, 51 support the conservative candidate, and 49 support the liberal candidate. Villagers get a payoff of þ10 if their candidate gets elected and a payoff of (cid:1)10 if the opposition candidate gets elected. But voting is a nuisance that results in a unit being subtracted from the payoff that a voter would otherwise receive. Those who stay at home and don't vote evade this cost but are rewarded or punished just the same as those who shoulder the cost of voting.

a. Why is it not a Nash equilibrium for everybody to vote?

b. Why is it not a Nash equilibrium for nobody to vote?

19. As a primitive exercise in mechanism design, imagine you are a planner who would like Adam and Eve to cooperate when playing the Prisoners' Dilemma. Since you can change the game by imposing fines on one or both of the players, it would be easy to achieve your objective if you were fully informed of everything that matters.

You could simply impose a heavy fine on any player who chooses hawk. Your problem is that you never get to see the payoff table, and the labeling of the strategies has gotten jumbled up, with the result that you don't know whether the cooperative strategy is hawk or dove. Can you think of a way of creating a game in which it is a Nash equilibrium for Adam and Eve to cooperate, without the need for you to know which strategy is which? The fallacy of the twins may provide some inspiration.

20. As in the previous problem, you are a planner who doesn't know which strategy is which in the Prisoners' Dilemma of Figure 1.3(a). You have probably figured out that you can make it rational for the players to choose the same strategy by fining them both if they choose different strategies. What will the payoff table of the resulting game look like to the players if you make the fine equal to (a) fifty cents; (b) four dollars. In which of the two games is it a Nash equilibrium to cooperate? Find another Nash equilibrium of this game. Which equilibrium is better for both players than the other?

21. Continuing the previous problem, find a fine that makes the new game into a version of the Stag Hunt Game.

22. You are a planner in the Tragedy of the Commons who is unable to redistribute the milk produced and doesn't know the milk production function. Use the idea introduced in the preceding problems to find a way that might lead rational players to use the common land efficiently.

23. Robert Nozick, a Harvard philosopher, believed that Newcomb's paradox shows that maximizing your payoff can be consistent with using a strongly dominated strategy. If true, this would be a disaster for game theory. Newcomb's paradox involves two boxes that possibly have money inside. Adam is free to take either the first box or both boxes. If he cares only for money, which choice should he make? This seems an easy problem. If dove represents taking only the first box and hawk represents taking both boxes, then Adam should choose hawk because this choice always results in his getting at least as much money as dove. Nozick says that hawk therefore "dominates" dove. However, there is a catch. It is certain that there is one dollar bill in the second box. The first box may contain nothing, or it may contain two dollar bills. The decision about whether there should be money in the first box is made by Eve, who knows Adam so well that she is always able to make a perfect prediction of what he will do. Like Adam, she has two choices, dove and hawk. Her dovelike choice is to put two dollar bills in the first box. Her hawkish choice is to put nothing in the first box. Her motivation is to catch Adam out. She therefore plays dove if and only if she predicts that Adam will choose dove. She plays hawk if and only if she predicts that Adam will choose hawk. Adam's choice of hawk now doesn't look so good. If he chooses hawk, Eve predicts his choice and puts nothing in the first box, so that Adam gets only the single dollar in the second box. If Adam chooses dove, Eve predicts his choice and puts two dollars in the first box for Adam to pick up. But how can it be right for Adam to choose dove when this choice is supposedly strongly dominated by hawk? Explain the payoffs in Adam's payoff matrix of Figure 1.9. Notice that Eve has four strategies: dd, dh, hd, and hh. For example, the strategy hd means that she plays hawk if Adam plays dove and dove if he plays hawk. We are told that she will actually choose dh, which means that she plays dove if Adam plays dove and hawk if he plays hawk. However, for hawk to dominate dove, it must be at least as good as dove for all of Eve's strategies. Is this true?

24. The late David Lewis, a Princeton philosopher, believed that Adam's payoff matrix in Newcomb's paradox should be assumed to be the same as his payoff matrix in the Prisoners' Dilemma of Exercise 1.13.1. Why doesn't such a model take account of the fact that Eve always predicts Adam's choice correctly, whatever it may be?

25. Relate the model of Newcomb's paradox illustrated in Figure 1.9 to the Transparent Disposition fallacy. If Lewis's model of Newcomb's paradox from the previous problem is combined with the assumption that Eve always mirrors his choice, why are we back with the twins fallacy?

26. Section 1.6.2 talks about a gene knowing something. How would you explain what this means to an old lady who objects that this evolutionary talk is nonsense because genes are just molecules and thus can't know anything at all?

27. Evolutionary games between relatives are considered in Section 1.6.2. Why is r = 1 the degree of relationship between full cousins?

28. Why did the biologist J.B.S. Haldane joke that he would jump in a river at the risk of his own life to save two brothers or eight cousins?

29. Alice's and Bob's payoffs in an evolutionary game are their biological fitnesses. If Alice and Bob were unrelated, the game would be the Prisoners' Dilemma of Figure 1.3(a). If their degree of relationship is r = 2, show that their payoff table is a version of the Stag Hunt Game.

30. Douglas Hofstadter used the column he once wrote for Scientific American to argue for a version of the twins fallacy (Section 1.3.3). The magazine followed up by proposing a Million Dollar Game. The rules of the game specify that if n readers enter the competition, then a prize of 1/n million dollars is awarded to a randomly chosen entrant. If entry is costless, what is a strictly dominant strategy for a reader? The selfless strategy is for a reader not to enter, but why can the categorical imperative not recommend this strategy? (Section 1.10) Why will readers all have to enter with the same positive probability in order to follow the categorical imperative? What considerations may be relevant in determining what this probability should be?

**Backing Up**

**2.1 Where Next?** Popular accounts of game theory seldom go beyond the simple payoff tables of the previous chapter, leaving all kinds of problems hanging in the air. How do the players of a game figure out what their strategies are? For a game like chess, this is a task of immense complexity. How do the players know what payoffs they will receive after each has chosen a strategy? What do the payoffs mean? As our discussion of the Prisoners' Dilemma in the previous chapter shows, we need to think of the payoffs as being measured in utils rather than dollars. But what precisely is a unit of utility? This chapter is the first of three in which these questions are answered systematically. Much of the fascination of game theory lies in learning how to handle the problems of timing, risk, and information that need to be solved in coming up with the answers. The current chapter concentrates on timing. How do we cope with games like chess, whose outcome is decided only after long sequences of moves? The next chapter concentrates on risk. How do we handle games like poker, in which the outcome is partly determined by chance? No matter how well you play your cards, you are not going to win if your opponents keep getting dealt better hands. The subject of information is too important to be hurried, and so we get by with saying as little as possible until it can be discussed with the attention it deserves in Chapter 12. The equally important subject of utility is more urgent, and so we study it in Chapter 4 immediately after discussing risk in Chapter 3. In the meantime, all talk of payoffs is avoided.

Some backing up on the previous chapter is therefore necessary. We need to reformulate ideas introduced in Chapter 1 without making premature appeals to the theory of utility. The expedient I employ is to express the ideas directly in terms of the players' preferences over the outcomes of a game. To simplify this task, it is necessary to restrict attention temporarily to strictly competitive games. These are two-player games in which Adam's and Eve's interests are diametrically opposed. A major advantage of this restriction is that the principle of backward induction can then be introduced in a context in which its role in analyzing games is least problematic.

**2.2 Win-or-Lose Games** The simplest kind of strictly competitive game allows only winning or losing. In such games, Adam and Eve distinguish only two outcomes, W and L. The symbol W denotes a win for Adam and a loss for Eve. Similarly, L denotes a loss for Adam and a win for Eve. I can remember desperately trying to lose when playing board games with my young children, but Adam and Eve are assumed to be more simply motivated. Whenever offered a choice between winning and losing, each player chooses to win. Economists summarize this behavior by saying that it reveals a preference for winning over losing. The assumptions over Adam's and Eve's preferences that we are making in win-or-lose games can be expressed in formal terms by writing: L ≻ W and W ≻ L. A E To write L ≻ W is to say that Adam strictly prefers winning to losing. In operational terms, he never chooses to lose when it is possible for him to win. Remember that writing W ≻ L also means that Eve strictly prefers winning to losing because, for her, W counts as a loss and L as a win.

**2.2.1 The Inspection Game** The Inspection Game is an example of a win-or-lose game that matters in real life. It is used here as a vehicle for introducing the basic ideas to be explored in this chapter in an informal way. The rest of the chapter then ties the ideas down more carefully. An unscrupulous firm has committed itself to discharging effluent into a river either today or tomorrow. It knows that the local environmental agency will be aware that it has made such a decision, but it isn't too worried because it can be convicted only if caught.

ht red handed by an inspector on the spot. However, the agency’s resources are so overstretched that it can afford to dispatch an inspector on only one of the two days. The problem for the agency is whether to send its inspector today or tomorrow.

Matching Pennies is a playground game that poses an identical strategic problem. Adam covers a penny with his hand. Eve guesses whether he is hiding a head or a tail. She wins the penny if she guesses right. He wins the penny if she guesses wrong.

The timing structure of the Inspection Game is illustrated in Figure 2.1(a). The firm’s opening move is represented by the node at the foot of the diagram. The two lines leading away from the node are labeled t for today and T for tomorrow. They represent the firm’s two choices of action: to pollute the river today or to pollute it tomorrow. Either of these decisions leads to a node representing a move for the environmental agency. In each case, the agency can decide whether to inspect today or tomorrow. The game ends after each player has moved. Each outcome of the game is labeled with W or L to represent a win or a loss for the firm.

The same figure will do equally well to describe the timing structure of Matching Pennies. Simply replace the firm and the agency by Adam and Eve. The symbol t will then have to stand for heads, and T for tails.

Something very important is missing from Figure 2.1(a). To represent the problem faced by the environmental agency properly, we need to indicate what the agency knows when it makes its decision. Game theorists use information sets for this purpose.

An appropriate information set for the Inspection Game has been drawn in Figure 2.1(b). This information set includes both of the agency’s decision nodes. Including both nodes in one information set means that, when the agency makes its decision at one of these nodes, it doesn’t know which of these two nodes the game has reached. That is to say, when the agency decides whether to inspect today or tomorrow, it doesn’t know in advance whether the firm has decided to pollute the river today or tomorrow.

When no information set has been drawn around a particular decision node, the assumption is that the player deciding at that node will know for sure that the game has reached that node when making a decision. In this case, one should properly draw a singleton information set that contains only that node, but life is usually too short for such niceties. As drawn, Figure 2.1(a) therefore represents the game in which some whistleblower can be counted on to call the agency before it decides on which day to inspect, with a reliable tip-off about the day on which the firm is going to pollute the river.

The equivalent situation in Matching Pennies would occur if Adam failed to hide his coin successfully, so that Eve could see what it was. Adam would be foolish to be so careless, but no more foolish than the folks who regularly play poker without ever learning to hold their cards close to their chests! If such infringements of the informational rules occur, it is important to recognize that we are not playing Matching Pennies or poker any more. We are playing some other game, which needs a new name—like Peeking Pennies or Suckers’ Poker. Our name for the new game created by changing the rules of the Inspection Game to allow a tip-off is the Tip-Off Game.

It isn’t hard to figure out what the agency should do in the Tip-Off Game. If the tip-off is that the firm has played t, then the agency should play t. If the tip-off is that the firm has played T, then the agency should play T. Whatever choice the firm makes, the agency will then win. The winning actions for the agency are indicated in Figure 2.1(a) by doubling the lines that represent them. Assuming that the firm knows that the agency will be tipped off, it will predict that the agency will choose the doubled line at whichever decision node it finds itself. If the firm plays t, it will therefore anticipate that the agency will also play t, with the result that the firm will lose. If the firm chooses T, it will anticipate that the agency will play T, with the result that the firm loses again. Either way, the firm loses. Since both of its choices lead to the same outcome, the firm will be indifferent between them. Both lines at its decision node have therefore been doubled in Figure 2.1(a).

The process of working backward through a game from the outcomes to the initial move, doubling the lines representing the best moves at each decision node, is called backward induction or dynamic programming. We don’t need such heavy machinery to solve the Tip-Off Game, but games don’t need to get much more complicated before it becomes useful to apply the principle of backward induction systematically.

However, we can’t solve all games by using backward induction. In particular, we can’t use it to solve the Inspection Game because the information set in Figure 2.1(b) prevents the agency from knowing which decision node the game has reached when it makes its decision. When deciding what action to take, it therefore doesn’t know which of t and T will generate the better outcome.

The information set that distinguishes Figures 2.1(a) and 2.1(b) therefore makes a big difference. The difference is reflected in the strategies available to the players in the different games obtained by assuming that there is or is not a tip-off. In both cases, the firm simply chooses t for today or T for tomorrow. In the Inspection Game, the agency also has only two strategies, t and T. Its outcome table therefore takes the simple form shown in Figure 2.2(b).

Drawing an outcome table for the Tip-Off Game isn’t so simple because the agency’s choice of action will depend on the whistleblower’s information about the firm’s choice. As a consequence, it is necessary to distinguish four strategies for the agency: tt, tT, Tt, and TT. The first letter in each pair says what action the agency plans to take if tipped off that the firm has chosen t. The second letter says what action the agency plans to take if tipped off that the firm has chosen T. We are then led to the outcome table of Figure 2.2(a).

We have already seen that the solution of the Tip-Off Game is for the agency to play the strategy tT, which calls for the agency to inspect on whatever day the tip-off says that the firm will pollute the river. It then doesn’t matter what the firm does because the agency will always win. In the outcome table of Figure 2.2(a), the column corresponding to the strategy tT correspondingly contains only the symbol L. In the language of the previous chapter, tT is a weakly dominant strategy for the agency.

However, the agency doesn’t get a tip-off in the Inspection Game. So what does game theory then recommend? To answer this question, we need to introduce mixed strategies.

2.2.2 Mixed Strategies

When Sherlock Holmes was puzzling about which station to leave the train when pursued by the evil Professor Moriarty, they were playing a version of the Inspection Game. But literature offers a more thoughtful analysis in Edgar Allan Poe’s Purloined Letter. The villain has stolen a letter, and the problem is where to look for it. Poe identifies the essence of the problem by first analyzing a playground game akin to Matching Pennies.

Poe imagines a boy who is such a good natural psychologist that he successfully predicts the thought processes of his opponents most of the time. He knows that a dull-witted opponent who chose heads last time will have just enough ingenuity to play tails when the game is played now but that a more subtle opponent will reason that such a switching strategy will be too easy to predict and so will stay with heads. A yet more subtle opponent will predict that the boy expects him to play heads for this reason and hence will play tails. An even more subtle opponent will play heads. And so on. Poe’s boy is therefore successful because he can extend chains of reasoning of the form

She thinks that I think that she thinks that I think...

one step further than his opponents.

When games are played in real life, this psychological element is paramount. Winning big in poker is about little else. For example, the poker column of the Independent newspaper of 20 May 1999 has this to say about whether Furlong should have called a half-million-dollar raise by Seed in the world poker championship: “Furlong knew that Seed knew that he was punting on all sorts of hands, and that Seed was primed to go over the top and blast him out. Seed probably knew that Furlong knew this. But what he did not know was that Furlong is the sort of man who virtually never folds an ace, no matter what.”

But how can one rational player outthink another? If Eve is rational, then she reasons optimally, and so Adam has only to figure out his opponent’s optimal line of reasoning to know precisely what she will be thinking. If he has trouble in doing so, he can look the answer up in a game theory book. Psychological questions therefore have no place in a discussion of the rational play of games. If everybody played poker rationally, there wouldn’t be a world poker championship because the winners and losers would be entirely determined by what cards the players were lucky enough to be dealt.

After the psychological escape route has been closed, the Inspection Game seems to leave game theory with a seemingly insoluble problem. If each player can predict how the other will reason, what prevents their thoughts revolving forever around the vicious circle shown in Figure 2.2(b)? The vertical arrows show the firm’s preferences, and the horizontal arrows show the agency’s preferences. None of the four cells of the outcome table can correspond to a solution of the game because each cell has an arrow leading away from it.

For example, if a game theory book were to recommend the strategy pair (t, T) as the solution of the Inspection Game, the agency wouldn’t follow its recommendation to play T because it would do better to play t if it thought that the firm were likely to follow the book’s recommendation by playing t. Similarly, (T, T) can’t be the solution because the firm would not play T if it thought that the agency were In the language of Section 1.6, none of the four strategy pairs of Figure 2.2(b) can count as a solution to the Inspection Game because none of them are a Nash equilibrium. At a Nash equilibrium, each player’s strategy choice must be a best reply to the strategy choices of the other players.

Does it follow that the Inspection Game has no solution? This wouldn’t be particularly paradoxical. After all, there is no real number x that solves the quadratic equation x² + 1 = 0. However, just as mathematicians extended the set of real numbers to the set of complex numbers to ensure that all quadratic equations have roots, so game theorists extend the set of pure strategies to the set of mixed strategies to ensure that all finite games have Nash equilibria.

A player uses a mixed strategy when his or her choice of pure strategy is made at random. For example, Adam might choose heads in Matching Pennies with probability 1/3 and tails with probability 2/3. But how can it ever be rational to choose at random?

In Matching Pennies, the answer is easy. The whole point of the game is to make your choice unpredictable. But if you want to be unpredictable, you can’t do better than to delegate your choice to a randomizing device like a roulette wheel or a pack of cards. Your only problem is to decide the probabilities with which each of your pure strategies is to be chosen.

In Matching Pennies, every child knows that the answer is to choose heads and tails with equal probability. Indeed, on the playground, Adam often makes a show of tossing his coin to lustrated in Figure 2.4(c), a tree is a connected graph with no cycles, in which a particular node has been singled out to be its root.

I pursue the botanical analogy by saying that the edges are branches of the tree. A terminal node of a finite tree is reached by starting at the root and moving along branches until one reaches a node from which no further progress is possible without retracing one’s steps. Such terminal nodes are sometimes called leaves.

When? The leaves of the tree correspond to the possible outcomes of the game. A play of a finite game is a connected chain of branches that starts at the root and ends at a leaf. A tree for a version G of Kayles is shown in Figure 2.5. The play shown in Figure 2.3 is indicated by thickening appropriate branches. Figure 2.6 shows a streamlined version of Kayles that suppresses forced moves and makes no reference to skittles.

What? Nodes in the tree other than leaves are called decision nodes. They represent the possible moves in the game. The root of the tree represents the first move of the game. The root of Kayles in Figure 2.6 is labeled a.

The branches leading away from a node represent the choices or actions available at that move. There are four choices available at the first move in the game G of Figure 2.6. These have been labeled l, m, n, and r. For example, n corresponds to the action in which player I opens the game G by taking one of the middle skittles.

Who? Each decision node is assigned a player’s name or number, so that we know who makes the choice at that move. In the game tree of Figure 2.6, player I chooses at the first move. If he chooses action n, then player II makes the next move. She has three choices labeled L, M, and R. If she chooses action R, then the game ends with a victory for her.

How Much? Each leaf must be labeled with the consequences for each player if the game ends in the outcome to which it corresponds. The game G is a win-or-lose game, and so its leaves are labeled with the symbols W and L.

2.3.4 Two Examples Kayles is a modern game invented by combinatorial mathematicians as a showcase for their talents. However, archeology reveals that games of perfect information are as old as civilization. Tic-Tac-Toe and Nim are examples of games of perfect information without chance moves that still get played.

Tic-Tac-Toe. Everybody knows the rules of Tic-Tac-Toe (or Noughts and Crosses). Its game tree is very large in spite of the simplicity of its rules. Figure 2.7 therefore shows only part of the tree. The labels W, L, and D indicate a win, loss, and a draw respectively for player I.

Nim. Unlike Tic-Tac-Toe, Nim is a win-or-lose game. It begins with several piles of matchsticks. Two players alternate in moving. When it is your turn to move, you must select one of the piles and remove at least one matchstick from that pile. In contrast to our version of Kayles, the last player to take a matchstick is the winner.

A dull art movie called Last Year in Marienbad consists largely of the characters playing Nim very badly. Perhaps their ineptitude is intended as a comment on the human condition. However, the only time I have seen Nim played for money, the guy in the bar who proposed playing seemed to know the optimal strategy given in Section 2.6 perfectly well!

## 2.4 Pure Strategies

We have already had a lot to say about strategies. When studying the Inspection Game, we even looked at mixed strategies in a game of imperfect information. But the time has now come to study pure strategies seriously.

A pure strategy for Alice in a game specifies an action at each of the information sets at which it would be her duty to make a decision if that information set were actually reached. If all the players in a game select a pure strategy and stick with it, then their decisions totally determine how a game without chance moves will be played.

In what remains of this chapter, we are considering only games of perfect information. In such a game, everybody knows exactly what point the game has reached whenever they make a decision. It is then relatively easy to draw the extensive form because we don’t need to bother with information sets at all. But Section 2.2.1 teaches us that games of imperfect information are easier in at least one respect—they have fewer pure strategies. This is because there can’t be more information sets than decision nodes. For example, the firm has two pure strategies in the Inspection Game of Figure 2.1(b). But when we delete the firm’s information set to obtain the Tip-Off Game of Figure 2.1(a), the firm’s number of pure strategies increases to four.

To determine a pure strategy in a game of perfect information, we must specify a plan of action at each and every node at which the player would have to make a decision if that node were reached. The version of Kayles shown as the game G in Figure 2.6 will serve as an example.

The nodes at which it would be up to player I to make a decision are labeled a, b, and c. A pure strategy for player I must therefore specify actions for him at each of these three nodes. Since there are 4 actions for player I at node a, 2 actions at node b, and 2 actions at node c, player I has a total of 4×2×2 = 16 pure strategies. These 16 pure strategies can be labeled: lll, llr, lrl, lrr, mll, mlr, mrl, mrr, nll, nlr, nrl, nrr, rll, rlr, rrl, rrr.

For example, the pure strategy labeled mlr means that action m is to be used if node a is reached, action l is to be used if node b is reached, and action r is to be used if node c is reached.

If player I uses pure strategy rrr, then it is impossible that nodes b or c will be reached, whatever player II may do. However, the formal definition of a strategy still requires the specification of an action at nodes b and c, even though the actions specified at these nodes will never have any affect on how the game gets played.

The nodes at which it would be up to player II to make a decision are labeled d, e, and f for the game G of Figure 2.6. A pure strategy for player II must therefore specify actions for player II at each of these three nodes. Since there are 3 available actions for player II at node d, 2 actions at node e, and 3 actions at node f, player II has a total of 3×2×3 = 18 pure strategies. These 18 pure strategies can be labeled: LLL, LLM, LLR, LRL, LRM, LRR, MLL, MLM, MLR, MRL, MRM, MRR, RLL, RLM, RLR, RRL, RRM, RRR.

The pure strategy labeled MLR means that action M is to be used if node d is reached, action L is to be used if node e is reached, and action R is to be used if node f is reached.

The play of Kayles shown in Figure 2.5 begins at the root a of the game G of Figure 2.6 with player I choosing action n. This leads to node f, at which player II chooses action R, which brings the game to an end at a leaf labeled with W to indicate a win for player I. Such a play of the game will be denoted by the sequence [nR] of actions that generates it.3 3 The square brackets emphasize that a play isn’t the same thing as a strategy.

What are the strategies that result in the play [nR] of G? The pair of strategies chosen by the players must be of the form (nxy, XYR), where nxy stands for any strategy for player I in which n is chosen at node a. There are 4 such strategies, namely nll, nlr, nrl, and nrr. Similarly, XYR stands for any strategy for player II at which R is chosen at node f. There are 6 such strategies, namely LLR, LRR, MLR, MRR, RLR, and RRR. So the total number of strategy pairs that result in the play [nR] is 4×6 = 24.

Figure 2.8 shows the strategic form of our variant of Kayles. The representation of G in Figure 2.6 as a game tree is called its extensive form. For each pair of strategies, the strategic form indicates what the outcome of the game will be if that pair of strategies is used. The rows of the matrix represent player I’s pure strategies, and the columns represent player II’s pure strategies. Thus, the cell in row nll and column LLR contains the letter L. This indicates that player I will lose the game if he uses pure strategy nll and player II uses pure strategy LLR. This fact was checked out in the previous paragraph by tracing the play [nR] that results from the use of strategy pairs of the form (nxy, XYR).

Von Neumann and Morgenstern called the strategic form of a game its normal form because they thought that the “normal” procedure in analyzing a game should be to discard its extensive form in favor of its strategic form. However, the sheer size of the strategic form of Figure 2.8 provides at least one reason why modern game theorists don’t always take their advice.

MRL 1 2 1 1 2 2 2 2 2 2 2 1 1 1 1

RRL 2 2 1 1 2 2 2 2 1 1 1 1 1 1 1 1

LLM 1 1 1 1 1 1 1 1 2 1 2 1 1 1 1 1

MLM 1 1 1 1 1 1 1 1 2 2 2 2 1 1 1 1

RLM 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1

LRM 1 1 1 1 2 2 2 2 2 1 2 1 1 1 1 1

MRM 1 1 1 1 2 2 2 2 2 2 2 2 1 1 1 1

RRM 1 1 1 1 2 2 2 2 1 1 1 1 1 1 1 1

LLR 2 2 2 2 1 1 1 1 2 1 2 1 1 1 1 1

MLR 2 2 2 2 1 1 1 1 2 2 2 2 1 1 1 1

RLR 2 2 2 2 1 1 1 1 1 1 1 1 1 1 1 1

LRR 2 2 2 2 2 2 2 2 2 1 2 1 1 1 1 1

MRR 2 2 2 2 2 2 2 2 2 2 2 2 1 1 1 1

RRR 2 2 2 2 2 2 2 2 1 1 1 1 1 1 1 1

Figure 2.8 The strategic form of the game G. Player II can guarantee winning by playing MLR no matter what pure strategy player I may choose, because every entry in the column corresponding to the pure strategy MLR is L.

## 2.5 Backward Induction

In the strategic form of Figure 2.8, all the entries in the column corresponding to player II’s pure strategy MLR are L. So if player II chooses MLR in our variant of Kayles, player I is doomed to lose, no matter what strategy he plays.

It turns out that one of the players in a win-or-lose game of perfect information without chance moves always has a pure strategy that guarantees victory no matter what the other player may do, but it isn’t by any means obvious that the strategic form of such a game must have either a column whose entries are all L or else a row whose entries are all W. This fact becomes obvious only when we apply backward induction to the extensive form of the game.

We used backward induction to solve the Tip-Off Game in Section 2.2.1. It requires starting from the end of the game and then working backward to its beginning. In this section, we offer an analysis of our variant of Kayles that shows how the same method may always be used to show that one or the other of the two players can guarantee victory in any win-or-lose game of perfect information without chance moves.

2.5.1 Subgames

In a game of perfect information, each node x other than a leaf determines a sub-game.4 The subgame consists of the node x together with all of the game tree that follows x. Figure 2.9 shows the six subgames of the game G of Figure 2.6. (Notice that the definition makes G a subgame of itself.)

2.5.2 Values

The value v(H) of a subgame H of G is W if player I has a strategy for H that wins the game H for him whatever strategy player II may use. Similarly, the value v(H) of the subgame H is L if player II has a strategy that wins the game H for her whatever strategy player I may use.

When we get to Von Neumann’s minimax theorem in Chapter 7, we will learn how to assign values to any two-player game in which the players have diametrically opposed preferences. The minimax theorem applies to all such strictly competitive games, including those with imperfect information and chance moves. But it is very unusual for a game that isn’t strictly competitive to have a value at all.

2.5.3 Analyzing the Game G

Consider first the one-player subgames G2, G4, and G5 of Figure 2.9. Player II wins G2 by choosing action L, and so v(G2) = L. (Recall that an outcome is labeled with L when player II wins.) Player I wins G4 or G5 by choosing action l, and so v(G4) = v(G5) = W.

Next consider the game G’ shown in Figure 2.10. This game is obtained from G by replacing the subgames G2, G4, and G5 with leaves labeled with their values. If G’ has a value, then G has a value as well, and v(G’) = v(G).

4It isn’t true that each node of a game of imperfect information determines a subgame. Each subgame must have a single node to serve as its root, but we can’t separate one node from its fellows in an information set for this purpose.

To prove this in the case when player I is the winner, we need to show that, if player I has a strategy s’ that always wins in game G’, then he necessarily has a strategy s that always wins in G. Why is this? Whatever strategy player II uses, player I’s choice of s’ in G’ results in a play of G’ that leads to a leaf x of G’ labeled with W. Such a leaf x may correspond to a subgame Gx of G. If so, then v(Gx) = W. Hence player I has a winning strategy s in Gx. It follows that player I has a winning strategy s in G, which consists of playing according to s’ until one of the subgames Gx is reached and then playing according to s.

Next consider the game G@ shown at the foot of Figure 2.10. This game is obtained from G’ by replacing the one-player subgames G’1 and G’3 by leaves labeled with their values. By the reasoning used before, if G@ has a value, then so does G’, and v(G@) = v(G’).

All of player I’s actions in the one-player game G@ lead to a leaf at which he loses. So the value of G@ is L. It follows that G also has a value, and v(G) = v(G’) = v(G@) = L.

That is to say, player II has a strategy that wins the game G, no matter what strategy is used by player I.

2.5.4 Finding a Winning Strategy

One way of finding a winning strategy for player I in G is to read it off from the strategic form given in Figure 2.8. However, except in very simple cases, this isn’t a sensible way of locating a winning strategy because the heavy labor involved in constructing the strategic form makes the method impractical.

A better way of finding a winning strategy is to mimic the method by means of which it was proved that a winning strategy exists for G. Begin by looking at the smallest subgames of G (those with no subgames of their own). In each such sub-game, double the branches that correspond to optimal choices in the subgame. Next pretend that the undoubled branches in these subgames don’t exist. This creates a

Figure 2.9 The subgames of G.

new game G*. Now repeat the procedure with G* and continue in this way until there is nothing left to do. At the end of the procedure there will be at least one play of G whose branches have all been doubled. These are the only plays that can be followed if it is common knowledge between the players that each will always try to win under all circumstances.

This procedure has been carried through for the game G in Figure 2.6. Four plays of the game have all their branches doubled, and each leads to a win for player II, thus confirming that she has a winning strategy.

A winning pure strategy can be read off directly from the diagram by choosing one of the doubled branches at each of player II’s decision nodes. In the case of G, the M branch is doubled at node d, the L branch at node e, and the R branch at node f. Player II therefore has only one winning pure strategy, namely MLR. If more than one branch were doubled at some of her decision nodes, player II would have multiple winning strategies.

Figure 2.10 Reducing the game G by backward induction.

## 2.6 Solving Nim

The procedure just described could also be carried out for Nim. However, as with Tic-Tac-Toe, it is hard work even to write down its game tree.

In the case of Nim, there is an elegant way of proceeding that avoids the necessity of constructing a game tree. This is illustrated using the version of Nim given in Figure 2.11. In this figure, the numbers of matchsticks in each pile have first been converted into decimal notation and then into binary notation.5

8 4 2 1 3 0 0 1 1 11 1 0 1 1 6 0 1 1 0

Figure 2.11 Nim with three piles of matchsticks.

Call a game of Nim balanced if each column of the binary representation has an even number of 1s and unbalanced otherwise. The example of Figure 2.11 is unbalanced because the eights column has an odd number of 1s (as do the fours column and the twos column). It is easy to verify that any admissible move in Nim converts a balanced game into an unbalanced game.6

The player who moves first in a balanced game can’t win immediately because a balanced game must have matchsticks in at least two piles. The player moving

5For example, the number whose decimal representation is 11 is the sum of 1 eight, 0 fours, 1 two, and 1 one. So its representation in binary form is 1011.

6At least one 1 in the binary representation of the pile from which matchsticks are taken will necessarily be changed to a 0. If the column in which this occurs had 2n ones, it will have 2n – 1 ones afterward.

Figure 2.12 Player I uses a winning strategy in Nim.

therefore can’t pick up the last matchstick right away because he or she is allowed to take matchsticks from only one pile at a time.

One of the players therefore has a winning strategy, which consists of always converting an unbalanced configuration into a balanced configuration. Using such a strategy guarantees that my opponent can’t win on the next move. Since this is true at every stage in the game, my opponent can’t win at all. But someone must pick up the last matchstick. If it isn’t my opponent, it must be me. So I must be using a winning strategy.

Since most games of Nim start out unbalanced, it is usually the first player to move who has a winning strategy. But if the original configuration of matchsticks is balanced, then the second player has a winning strategy.

Figure 2.12 shows a possible play of the version of Nim given in Figure 2.11.

Figure 2.11. Player I is using a winning strategy. It is worth noticing that, once player I is faced with only two piles of matchsticks with equal numbers of matchsticks in each, then he can win by "strategy stealing." All he need do is to take as many matchsticks from one pile as player II just took from the other.

## 2.7 Hex

The game of Hex was invented by Piet Hein in 1942. The same John Nash who formulated the idea of a Nash equilibrium came up with an identical set of rules in 1948. Nash is said to have been inspired by the hexagonal tiling in the men's room of the Princeton mathematics department, but he thinks this story is apocryphal.

Hex is a game played between Circle and Cross on a board made up of n² hexagons arranged in a parallelogram, as illustrated in Figure 2.13(a). At the beginning of the game, each player's territory consists of two opposite sides of the board. The players take turns in moving, with Circle going first. A move consists of taking possession of a vacant hexagon on the board by labeling it with your emblem. The winner is the first to link their two sides of the board with a continuous chain of hexagons labeled with their emblem. In the game that has just concluded in Figure 2.13(b), Cross was the winner.

Aside from its association with Nash, Hex is interesting for two reasons. The first point of interest is that Hex is a win-or-lose game, although it seems possible at first sight that it might end in a draw. Since all win-or-lose games of perfect information without chance moves have a value, we know that one of the players has a pure strategy for Hex that guarantees victory whatever the other player may do. It isn't known what the winning strategy is when n is reasonably large, but the second interesting feature of Hex is that we can nevertheless show that the player with the winning strategy is Circle.

2.7.1 Why Hex Can't End in a Draw Think of Circle's hexagons as water and Cross's hexagons as land. When all the hexagons have been labeled, either water will then flow between the two lakes originally belonging to Circle, or else the channel between them will be dammed. Circle wins in the first case, and Cross in the second.

This simple argument is intuitively compelling, but it turns out not to be so easy to back it up with a rigorous proof. So why do mathematicians bother? The answer is that the history of mathematics is awash with propositions that seemed obviously true but eventually turned out to be false. However, the Mad Hatter in the margin invites you to skip forward to Section 2.7.2 if you aren't interested in the following math sketch of David Gale's proof that Hex can't end in a draw.

Gale uses an algorithm that requires starting from a point off the corner of the board, as shown in Figure 2.14(a). You must then trace out a path so that the next segment of the path always has a circled hexagon on one side and a crossed hexagon on the other. You could do this by immediately going back the way you just came, but retracing your steps in this way isn't allowed.

We need to show that such a path can neither terminate on the board, nor return to a point it has visited before. Since the Hex board is finite, the path must then terminate at one of the points off the corners of the board other than that from which it started. It follows, as illustrated in Figure 2.13(b), that one of the two opposite sides of the board must be linked. So Hex can't end in a draw.

Figure 2.14(a) shows a path that has reached a point p in the interior of the board. We need to show that the path can be continued. To reach p, the path must have just passed between a crossed hexagon H and a circled hexagon J. Since p is in the interior of the board, there has to be a third hexagon K for which p is a vertex. If K is crossed, as in Figure 2.14(a), the path can be continued by passing between J and K. If K is circled, the path can be continued by passing between H and K.

If p is on the edge of the board, the argument has to be modified slightly, but it still works. The argument fails only if p is one of the four points off the corners of the board. So these are the only points where the path can terminate.

Figure 2.14(b) shows a path returning to an interior point q that it has visited before. To do this, the path violates the rule that it must keep a crossed hexagon on one side and a circled hexagon on the other. To prove by contradiction that a path can never loop back on itself without violating this rule, let q be the first point that gets revisited. For q to be visited at all, the three hexagons L, M, and N with a common vertex at q can't all have the same label. Suppose that L is crossed, and the other two hexagons are circled, as in Figure 2.14(b). The path must then have passed between L and M, and between L and N on its first visit. Since q is the first revisited point on the path, the path can't have gotten back to q via the point r or the point s. It can have gotten back to q only via t. But M and N are both circled, and so this is impossible. As before, the argument has to be adapted slightly if q is on the edge of the board, but it still works.

2.7.2 Why Circle Has a Winning Strategy Nash gave a "strategy-stealing" argument that shows that if Cross has a winning strategy, then so does Circle. Since it's impossible for both players to win, it therefore can't be true that Cross has a winning strategy. But someone has a winning strategy. Since it isn't Cross, it must be Circle.

If Cross has a winning strategy, how would Circle steal it? Nash argued that Circle could follow the following instructions:

## 1. At the first move, circle a hexagon at random

2. At later moves, pretend that the last hexagon you circled is unlabeled. Next pretend that the remaining circled hexagons are all crossed and the crossed hexagons are all circled. You have now imagined yourself into a position to which Cross's winning strategy applies. Circle the hexagon that Cross would choose in this position if she were to use her winning strategy. The only possible snag is that this hexagon may be the hexagon you are only pretending is unlabeled. If so, then you don't need to steal Cross's winning move for the position because you have already stolen it. Just circle a free hexagon at random instead.

This strategy wins for Circle because he is simply doing what supposedly guarantees Cross a win—but one move earlier. The presence on the board of an extra hexagon labeled with a Circle may result in his winning sooner than Cross would have, but we won't hear him complaining if this should happen!

## 2.8 Chess

Computers can beat anybody at checkers, but world-class players can still beat computers at chess most of the time. However, when computer programs are eventually developed that beat even the best human players, it won't be because game theorists have worked out the optimal way to play. Chess is so complicated that its solution will probably never be known for certain—and this is just as well for people who play for fun. What would be the point of playing at all if you could always look up the optimal next move in a book?

However, game theory isn't entirely helpless. Nobody can find Bigfoot or the Loch Ness Monster because they don't exist, but this isn't the reason that game theorists can't find the solution to chess. We can at least prove that chess actually does have a value.

Strictly Competitive Games. The games studied so far in this chapter have nearly all been win-or-lose games. The exception was Tic-Tac-Toe, which can end in a draw. Chess also has three possible outcomes: W, L, and D: We take player I to be White and player II to be Black, and so W denotes a win for White and a loss for Black.

To write a ≿ᵢ b means that player i likes b at least as much as a. To write a ≻ᵢ b means that player i strictly prefers b to a. That is to say, he or she never chooses a when b is on the table. To write a ~ᵢ b means that player i is indifferent between a and b. To say that a ≿ᵢ b is therefore the same as saying that either a ≻ᵢ b or else a ~ᵢ b.

In a strictly competitive game, the players' aims are diametrically opposed. Whatever is good for one is bad for the other. In mathematical terms, this means that for each outcome a and b, a ≻₁ b ⇔ b ≻₂ a.

Chess is therefore a strictly competitive game, as the players' preferences are: L ≻₁ D ≻₁ W, L ≺₂ D ≺₂ W.

The fact that chess has a value will be deduced from a more general theorem that tidies up the account of backward induction given in Section 2.5. When the theorem says that player i can force an outcome in a set S, it means that player i has a strategy that guarantees that the outcome will be in the set S, whatever the other player does. The notation ¬S is used for the complement of a set S. In the theorem, ¬T therefore consists of all outcomes of the game that aren't in the set T.

Theorem 2.1 Let T be any set of outcomes in a finite two-player game of perfect information without chance moves. Then, either player I can force an outcome in T, or player II can force an outcome in ¬T.

Proof Forget all about the players' preferences in the game. We are then free to relabel all the outcomes in T with W, and all the outcomes in ¬T with L. The theorem then reduces to showing that any finite, win-or-lose game has a value. The argument of Section 2.5.3 can be recycled for this purpose, but since we are now proving a formal theorem, we ought to be more careful about the mathematical details.

Step 1. The rank of a game is the number of branches in its longest possible play. So a game of rank 1 consists of just a root and some leaves. If player I chooses at the root, then he can win immediately if one of the leaves is labeled with W. Otherwise, all the leaves of a win-or-lose game are labeled with L, and so player II can force a win without doing anything at all (as in the game G@ of Figure 2.10). Either way the game has value. Since similar reasoning applies if player II chooses at the root, it follows...

that any win-or-lose game H of rank 1 has a value v(H) (Section 2.5.2).

Step 2. Now suppose that, for some value of n, all win-or-lose games of rank n have a value. We will show that any win-or-lose game H of rank n+1 must then have a value as well.

Locate the last decision node x on each play of length n+1 in H. Now throw away anything that follows such a node. The nodes x then become leaves of a new game H' when we label each x with the value v(H_x) of the subgame H_x of H rooted at x. Such subgames are of rank 1 and hence must have a value by Step 1.

The game H' is of rank n, and so it has a value. Suppose it is player I who has a strategy s' that wins H' whatever player II may do. The use of s' then guarantees that H' will end at a leaf of H' labeled with W. If this leaf corresponds to a subgame H_x of H, then v(H_x) = W, and so player I has a winning strategy s_x in H_x. So player I can force a win in H by playing s' in H' and s_x in each subgame H_x for which he has a winning strategy. The same reasoning applies if it is player II who has a winning strategy in H'. Thus one of the players can force a win in H, and so H has a value.

Step 3. The final step is to apply the Principle of Induction. Step 1 says that all win-or-lose games of rank 1 have a value. Step 2 then implies that all win-or-lose games of rank 2 also have a value. Step 2 can then be applied again to show that all win-or-lose games of rank 3 have a value. And so on.

All finite win-or-lose games of perfect information without chance moves therefore have a value, and so the theorem is proved.

2.8.1 Values of Strictly Competitive Games

A Mad Hatter in the margin is usually running away to another section, and beginners would be advised to follow him. Here he isn't running away, although he looks as though he would like to. This means that something tougher than usual is coming up, but that the urge to rush on by should be resisted.

An outcome v is said to be a value of a two-player game G if and only if player I can force an outcome in the set W = {u: u ⪰ v} and player II can simultaneously force an outcome in the set L = {u: u ⪯ v}.

For example, if White has a strategy that can force a draw or better for him and Black has a strategy that can force a draw or better for her, then the value of chess is D. In this case, W_v = {D, W} and L_v = {L, D}. If it turns out that the value of chess is W, then W_v = {W} and L_v = {L, D, W}.

Without loss of generality, it will be assumed that player I isn't indifferent between any pair of outcomes of G. Thus the outcomes in the set U = {u_1, u_2, ..., u_k} of all possible outcomes of G can be labeled so that u_1 ≻_1 u_2 ≻_1 ... ≻_1 u_k. Player II's preferences then satisfy u_1 ≻_2 u_2 ≻_2 ... ≻_2 u_k. Figure 2.15 illustrates what it means for such a game to have a value v.

Corollary 2.1 Any finite, strictly competitive game of perfect information without chance moves has a value.

Proof Let W_v be the smallest set into which player I can force the outcome. If v = u_j, player I can't force the outcome to be in W_{u_{j+1}} because this is a smaller set than W_v. So player II must be able to force an outcome in \ W_{u_{j+1}} = L_v, by Theorem 2.1.

Corollary 2.2 Chess has a value.

Proof Chess is a finite, strictly competitive game of perfect information without chance moves.

2.8.2 Saddle Points

A strategy pair (s, t) is a saddle point of the strategic form of a strictly competitive game if the outcome that results from the use of (s, t) is no worse for player I than any outcome in the column corresponding to t and no better for him than any outcome in the row corresponding to s.

Corollary 2.3 The strategic form of a finite, strictly competitive game of perfect information without chance moves always has a saddle point (s, t).

Proof Let s be a strategy that guarantees player I an outcome no worse than the value v of the game. Then each entry in row s of the strategic form must be no worse than v for player I. Let t similarly guarantee player II an outcome no worse than v. Then each entry in column t must be no worse than v for player II. Because the game is strictly competitive, each entry in column t is therefore no better than v for player I. The actual outcome that results from the play of (s, t) must therefore be no worse and no better for player I than v. Since players are assumed not to be indifferent between outcomes in this section, the result of playing (s, t) must therefore be exactly v.

Theorem 2.2 If the strategic form of a strictly competitive game G has a saddle point (s, t) for which the corresponding outcome is v, then the value of G is v.

Proof Since v is the worst outcome in its row for player I, he can force an outcome at least as good as v by playing s. Since v is the best outcome in its column for player I, it is the worst in its column for player II, so she can force an outcome at least as good for her as v by playing t.

I find that serious chess players are curiously uninterested in game theory, but when they can be persuaded to offer an opinion, they always guess that the value of chess is D, which would mean that both players have strategies that can force a draw or better. Figure 2.16 is a notional strategic form for chess drawn on the assumption that the experts are right. In this figure, s is a pure strategy that forces a draw or better for player I, and t is a pure strategy that forces a draw or better for player II. By Corollary 2.3, the pair (s, t) is then a saddle point of the strategic form of chess.

## 2.9 Rational Play?

What advice should a game theory book give to two people about to play a strictly competitive game G of perfect information without chance moves?

If the game has value v, the answer may seem easy. Surely both players should simply choose pure strategies that guarantee each an outcome no worse than v. If such a pair (s, t) of pure strategies is used, then the game will end in some outcome that both players regard as being equivalent to v. But things are seldom so easy in game theory!

2.9.1 Nash Equilibrium

The pair (s, t) certainly meets one of the criteria that must be satisfied if it is to be proposed by a game theory book for general adoption as the rational solution of a game. The criterion is that (s, t) should be a Nash equilibrium. This means that each of the pure strategies in the pair (s, t) must be a best reply to the other (Section 1.6).

In a strictly competitive game, a pair (s, t) is a Nash equilibrium if and only if it is a saddle point of the strategic form of the game. The fact that v is best in its column makes s a best reply to t for player I. Since the two players have opposing preferences, the fact that v is worst in its row for player I makes it best in its row for player II. Thus t is a best reply to s for player II.

For example, in the strategic form of Figure 2.8, all pure strategy pairs in which player II uses MLR are Nash equilibria. That is to say, every outcome in the ninth column of the strategic form corresponds to a saddle point.

It would be self-defeating for a game theorist to publish a recommendation for each player that wasn't a Nash equilibrium. If the advice were generally adopted, then it would be common knowledge how the game would be played. However, if player I knows that player II is sufficiently rational to carry out the book's advice by playing t, then he would be stupid to follow the book's advice to play s unless s is a best reply to the strategy t that he knows player II is going to choose. Similarly, if player II knows that player I is sufficiently rational to carry out the book's advice by playing s, then she would be stupid to follow the book's advice to play t unless t is a best reply to s.

Critics sometimes complain that the idea of a Nash equilibrium gets used even when there isn't any reason to suppose that the players will behave as though they were rational. I think that such attempts to apply game theory in situations to which it isn't applicable deserve all the criticism they get. In particular, rational players who know that their opponents are irrational won't necessarily be content to play so as to guarantee themselves the value of a strictly competitive game. They will want to exploit the folly of their opponent in an attempt to get more than its value.

2.9.2 When Are People Rational?

Traditional economics is somewhat shakily founded on the assumption that rationality commonly reigns in the commercial and business world, but modern economists are much less ready than their predecessors to assume that economic agents will always behave rationally.

Perhaps the fact that real people often behave irrationally is just as well for those games that are played mostly for fun. Watching two people play poker optimally would be about as interesting as watching paint dry—and nobody would play chess at all if it were known how to play it optimally.

However, if we can't count on the players in a game behaving rationally, then we have seen that orthodox game theory won't help us predict how they will play. So when is it reasonable to assume that the players in a game will behave as though it were common knowledge that they are all rational?

Other game theorists are sometimes more optimistic, but my own view is that it is very risky to use game theory for predictive purposes when none of the following criteria are satisfied:

*   The game is simple.

*   The incentives for playing well are adequate.

*   The players have played the game many times before, and hence have had much opportunity for trial-and-error learning.

In laboratory experiments with human subjects, Nash equilibrium normally predicts human behavior quite well when all three criteria are satisfied. The explanation usually offered is that nothing then obstructs the convergence of trial-and-error adjustment processes like those mentioned in Section 1.6. After the process has converged on a Nash equilibrium, the players are seldom able to explain why their final choice of strategy is optimal, but it is enough that they are behaving as though they had made such an optimal choice.

a rational choice.

Out of the laboratory, it isn’t so easy to tie down the environment within which a game is played. However, the second and third criteria are satisfied, for example, when poker is played by experts at the world poker championships. Moreover, while poker isn’t as simple as Tic-Tac-Toe or Nim, it is simple when compared to chess. That is to say, all its many variants, like Texas Hold’em or Seven Card Stud, can be analyzed successfully in principle. The first criterion is therefore also satisfied to some degree. So it is reassuring that play at these championships is much closer to what game theory predicts for rational players than in nickel-and-dime neighborhood games. For example, game theory recommends much bluffing on very bad hands (Section 15.2). Champions know this, but nickel-and-dime players tend to bluff only on middle-range hands that might win anyway.

In biological games, neither the first nor the second criterion commonly holds. Sometimes the advantage that accrues to the fitter of two strategies is so slight as to be imperceptible when a game is played just once. But the third criterion applies with a vengeance since evolution may have had millions of years to learn the optimal strategy by trial and error. Evolutionary biology is therefore an important area of application for the idea of a Nash equilibrium.

In telecom auctions, licenses to broadcast on specified chunks of the radio spectrum have sometimes been sold for several billion dollars. In this context, it is the second criterion that applies with a vengeance, and the third criterion doesn’t apply at all. However, the telecom companies use the idea of a Nash equilibrium in deciding how to bid because they don’t expect anyone to bid stupidly when such large amounts of money are on the table.

13 Against different opponents each time. If you play repeatedly against the same opponent, the repeated situation must be modeled as a single ‘‘supergame.’’

2.9.3 Subgame-Perfect Equilibrium The strategy pair (mlr, MLR) is a Nash equilibrium in the strategic form of Kyles given in Figure 2.8, but you won’t come up with this strategy pair by applying backward induction in the extensive form of the game given in Figure 2.6. The strategy pairs selected by backward induction are those that correspond to branches that are doubled in this figure. Backward induction therefore always selects MLR for player II but leaves player I free to choose between any strategy of the form xll. However, mlr doesn’t take this form.

Backward induction doesn’t select mlr because it requires player I to plan to make an irrational choice at node c. Choosing r at node c is irrational because player I can win at node c by playing l rather than losing by playing r. The fact that such an irrational plan is built into mlr doesn’t prevent the strategy being part of a Nash equilibrium because, if player II uses her Nash equilibrium strategy MLR, then node c won’t be reached. So player I will never actually be called upon to make the irrational choice that he would make if node c were reached.

The lesson is that Nash equilibria only ensure that players will behave rationally at nodes on the equilibrium path—the play of the game followed when the players use their equilibrium strategies. Off the equilibrium path, Nash equilibria allow the players to plan to behave in all kinds of crazy ways.

For example, if the value of chess is D, then White has a pure strategy s that guarantees him a draw or better, but he can’t do any better than a draw if Black uses the pure strategy t that guarantees her a draw or better. However, real people sometimes make mistakes. What if Black makes a momentary error that results in a subgame being reached that wouldn’t have been reached if she hadn’t deviated from t? The use of strategy s still guarantees a draw or better for White because s guarantees a draw whether Black plays well or badly, but it may be that White can now do better than forcing a draw. Perhaps he has a winning strategy in the subgame H reached as a result of Black’s blunder. Why should he then stick with s? If another strategy s’ guarantees a victory for White in H, he does better by switching from s to s’.

A game theory book would therefore fail in its duty if it were content to recommend any Nash equilibrium of Chess as its solution. The book should offer more refined advice. The conservative candidates for such a refinement are the strategy pairs (s,t) selected by backward induction. Such a strategy pair isn’t only a Nash equilibrium in the whole game, it also induces Nash equilibrium play in every subgame H—whether or not H is reached in equilibrium.

Following Reinhard Selten, a pair of strategies with this property is called a subgame-perfect equilibrium. A Nash equilibrium can fail to be subgame perfect only if it is certain that some subgame won’t be reached when the equilibrium strategies are used, but this often happens.

2.9.4 Exploiting Bad Play?

We will use subgame-perfect equilibria a great deal, and so it is important to ask when it is safe to recommend a subgame-perfect equilibrium as the solution of a game. Section 2.9.1 reminds us that orthodox game theory assumes that we begin playing a game with strong evidence that all the players are rational. But what if one of the players contradicts this evidence by playing badly?

Consider the example of Figure 2.17, which is like chess to the extent that players I and II move alternately, and the labels W, L, or D refer to a win, draw, or loss for player I. However, unlike chess, the players are assumed to care about how long the game lasts. Player I’s preferences are given by W1 ≺ W2 ≺ ⋯ ≺ W101 ≺ D1 ≺ L1.

Player II is assumed to hold opposing preferences. This makes the game strictly competitive. The doubled branches in Figure 2.17 show the result of applying backward induction.

Since only one branch is doubled at each node, there is only one subgame-perfect equilibrium. This calls on player II to play down at node 50. Is this good advice? The answer depends on what she knows about player I. The advice is sound if she is so sure that he is rational that no evidence to the contrary will change her mind. A rational player I would certainly play down if he found himself at node 51 because this results in an immediate victory for him. Hence player II had better not let node 51 be reached. She should settle instead for a draw by playing down at node 50.

However, node 50 wouldn’t have been reached if player I hadn’t played across on twenty-five consecutive occasions when it was rational to play down. This fact isn’t consistent with player II’s original belief that player I is rational. However, she may reason that even Nobel prize winners sometimes make mistakes. If so, then she can attribute player I’s behavior in always playing across to twenty-five independent random errors.

At each move, she can argue, player I intended to play down, but fate intervened by distracting his attention or jogging his elbow, so that he ended up playing across. She will assign only a small probability p to his making each such blunder, and so the probability p25 of his making twenty-five independent mistakes will be almost infinitesimal.14 But it remains logically coherent for her to put her faith in this extremely unlikely eventuality, rather than give up believing that her opponent is highly likely to play rationally in the future.

Of course, in real life, nobody seeking to explain the behavior of an opponent in chess who has just made twenty-five consecutive bad moves would think it plausible that he really meant to make a good move each time but somehow always contrived to move the wrong piece by mistake. The natural conclusion to draw from observing bad play is that the opponent is a weak player. The question then arises as to how to take advantage of his weakness.15

In the game of Figure 2.17, player I’s weakness seems to be a fixation on always playing across. If player II thinks this explanation of his behavior is likely on finding herself at node 50, she may care to chance playing across herself. The risk is that player I may deviate from his previous pattern of behavior by playing down at node 51. If so, then player II has passed up the chance for a draw to no avail. However, if player I continues to play across at node 51, then she can win at node 52 by playing down.

The moral is that subgame-perfect equilibria are fully defensible only in certain games. In short games, there won’t be enough time for sufficient evidence to accumulate to reverse the players’ initial belief that everyone is rational. In games with enough chance moves and information sets, the leading explanation for play having reached unanticipated subgames will usually be the vagaries of chance, rather than stupid play by other players.

However, even in long games of perfect information, subgame-perfect equilibria may still be useful. Section 14.4 explains how such games can be modified by introducing chance moves and information sets into the rules of the game, so as to model the systematic irrationalities of their opponents that the players would otherwise use to explain arriving at unanticipated subgames. We thereby construct a game in which it is sensible to study subgame-perfect equilibria.

When critics attack the idea of a subgame-perfect equilibrium, the appropriate response for a game theorist is therefore similar to what was said in Section 1.4.1 when responding to the criticism that game theorists assume that people are selfish. Such critics would usually do better to stop attacking the methodology of game theory and start criticizing the relevance of the particular game being studied to the real-world problem that it supposedly models.

## 2.10 Roundup

This chapter has looked at strictly competitive games of perfect information with no chance moves. These games have been studied without appealing to utility theory by expressing the players’ preferences directly in terms of the possible outcomes of the game. Chess and Tic-Tac-Toe are examples.

A strictly competitive game has two players whose preferences over the possible outcomes of the game are diametrically opposed. The simplest kind of strictly competitive game is a win-or-lose game. In such games, there must be a winner and a loser, and both players prefer...

winning to losing. Examples of win-or-lose games about which we had something to say are Nim and Hex. To write down the rules of a game in a precise form, it is necessary to begin by asking the questions who, what, when, and how much? The answers are recorded with the help of a game tree. Chance moves arise when the answer to the question who is that the relevant decision is made by rolling dice or using some other randomizing device. Shuffling and dealing in poker is a good example of a chance move.

It may sometimes be risky to do so because your opponent could be a hustler setting you up for a sting. But no possible advantage can accrue to player I here from playing across twenty-five times in a row when he can win immediately on each occasion just by playing down.

Once a game tree has been constructed, further vital questions need to be asked. We need to be told what the players know and when they know it. Information sets are used to record the answers. A game tree with its associated information sets is called the extensive form of a game. It tells us everything available about the rules of the game.

To include a number of decision nodes in the same information set is to specify that a player doesn’t know which of the nodes within that information set the game has reached when he or she decides what action to take next. The game of Matching Pennies provides an example. When Eve guesses heads or tails, she doesn’t know whether Adam previously hid a head or a tail. Her two decision nodes therefore belong in the same information set.

Matching Pennies is an example of a game of imperfect information because it has an information set that contains more than one decision node. In such games, a player isn’t informed about some aspects of the past history of the game that might be useful when making a move. In games of perfect information like chess, all the past history of the game is always an open book. Every information set is therefore a singleton, containing exactly one decision node. When a decision node in a game tree isn’t enclosed in an information set, the implication is that the information set hasn’t been drawn because it is a singleton. Game trees drawn with no information sets at all should therefore be assumed to be games of perfect information.

A pure strategy specifies an action at each of a player’s information sets in the extensive form of a game. Once the players have chosen their pure strategies, the outcome of a game without chance moves is then completely determined. The strategic form of a game is a table that records the outcome corresponding to each possible profile of pure strategies the players might choose. A Nash equilibrium is a strategy profile in which each player’s choice of strategy is a best reply to the strategies chosen by the other players. In order to qualify as a candidate for the solution of a game, a strategy profile must be a Nash equilibrium.

In a game of imperfect information like Matching Pennies or the Inspection Game, it sometimes makes sense to delegate your choice of action to a randomizing device. A player who does so is said to be using a mixed strategy. A player who makes a deterministic choice is then said to be using a pure strategy. This chapter avoids saying much about probability by not allowing chance moves and restricting attention to games of perfect information for which mixed strategies are not needed.

Strictly competitive games of perfect information can be solved by backward induction. You take subgames whose solution is known and replace them in the game tree by new leaves labeled with the solution outcome of the subgame. Starting with the smallest subgames and reducing larger and larger subgames, you eventually end up with a game that has only one node, which is labeled with the solution outcome of the game with which you started.

A subgame-perfect equilibrium is a strategy profile that isn’t only a Nash equilibrium in the whole game but also calls for a Nash equilibrium to be played in every subgame—whether or not the subgame is reached when everybody plays their equilibrium strategies. Not all Nash equilibria are subgame perfect. Nash equilibria that aren’t subgame perfect involve at least one strategy that calls for suboptimal play in a subgame that lies off the equilibrium path. The strategy therefore passes the best-reply test in the game as a whole but fails the best-reply test in some unreached subgame. Backward induction necessarily generates subgame-perfect equilibria.

Backward induction is unproblematic in win-or-lose games. The only time it fails to find a winning strategy for you is when you have no possibility of winning at all against a rational opponent. In strictly competitive games like chess that have more than two possible outcomes, backward induction will find the value of the game, together with a pure strategy whose play guarantees that the outcome will be no worse for you than the game’s value. The guarantee applies whether or not your opponent plays rationally. If your opponent is rational, then you can get no more than the value of the game because backward induction will also find a pure strategy that guarantees an outcome for her that is no worse than the game’s value. You will then both be playing a subgame-perfect equilibrium that generates the value of the game.

However, opponents are not always rational. Sometimes they can be very stupid indeed. It is therefore not necessarily a good idea to use your backward induction strategy because it sacrifices any chance you might have of exploiting any systematic mistakes you might observe your opponent making. But remember that it is risky to deviate from the backward induction strategy because the world is full of hustlers who pretend to be stupid precisely in order to make money off of those who try to exploit them.

## 2.11 Further Reading

Lectures on Game Theory, by Robert Aumann: Westview Press (Underground Classics in Economics), Boulder, CO, 1989. These are the classroom notes of one of the great game theorists.

Winning Ways for your Mathematical Plays, by Elwyn Berlekamp, John Conway, and Richard Guy: Academic Press, New York, 1982. This is a witty and incredibly inventive book, which is largely about solving complicated games by backward induction.

Mathematical Diversions and Hexaflexagons, by Martin Gardner: University of Chicago Press, Chicago, 1966 and 1988. The books gather together many delightful games and brainteasers from the author’s long-standing column in Scientific American.

The Game of Hex and the Brouwer Fixed-Point Theorem, by David Gale: American Mathematical Monthly 86 (1979), 818–827. Who would have thought that the fact that Hex can’t end in a draw is equivalent to the Brouwer fixed-point theorem?

## 2.12 Exercises

1. Figure 2.18 shows the tree of a strictly competitive game G of perfect information without chance moves.

a. How many pure strategies does each player have?

b. List each player’s pure strategies using the notation of Section 2.5.

c. What play results from the use of the pure strategy pair (rll, LM)?

d. Find all pure strategy pairs that result in the play [rRl].

e. Write down the strategic form of G.

f. Find all the saddle points.

2. Two players alternate in placing dominoes on an m x n chess board so as to cover two squares exactly. The first to be unable to place a domino is the loser. Draw the game tree for the case m=2 and n=3.

3. Figure 2.19 is a skeleton for the tree of a game called Blackball. A committee of three club members (I, II, and III) has to select one from a list of four candidates (A, B, C, and D) as a new member of the club. Each committee member is allowed to blackball (veto) one candidate. This right is exercised in rotation, beginning with player I and ending with player III. Why is Blackball not a strictly competitive game?

Label each decision node on a copy of Figure 2.19 with the numeral of the player who decides at that node. The branches representing choices at the node should be labeled with the candidates who have yet to be blackballed. Each leaf should be labeled with the letter of the candidate elected to the club if the game ends there. How many pure strategies does each player have? What information hasn’t been supplied that is necessary to analyze the game?

4. Begin to draw the game tree for chess. Include at least one complete play of the game in your diagram.

5. Two players alternate in choosing either 0 or 1 forever. A play of this infinite game can therefore be identified with a sequence of 0s and 1s. For example, the play 101000... began with player I choosing 1. Then player II chose 0, after which player I chose 1 again. Thereafter both players always chose 0. A sequence of 0s and 1s can be interpreted as the binary expansion of a real number x satisfying 0 ≤ x ≤ 1. For a given set E of real numbers, player I wins if x ∈ E but loses if x ∉ E. Begin to draw the game tree.

6. Apply backward induction to the game G of Exercise 2.12.1. What is the value of G? What is the value of the subgame starting at node b? What is the value of the subgame starting at node c? Show that the pure strategy rrr guarantees that player I gets the value of G or better. Why is this pure strategy not selected by backward induction?

7. Apply backward induction to the 2 x 3 version of the domino-placing game of Exercise 2.12.2. Find the value of the game, and determine a winning strategy for one of the players.

8. Who would win a game of Nim with n ≥ 2 piles of matchsticks of which the kth pile contains 2^(k-1) matchsticks? Describe a play of the game in which n=3, and the winner plays optimally while the loser always takes one matchstick from a pile with the median number of matchsticks. (The median pile is the middle-sized pile.) Do the same for 2n-1 piles, of which the kth pile contains k matchsticks.

9. Who wins in the domino-placing game of Exercise 2.12.2 when (a) m and n are even; (b) m is even and n is odd; (c) m=n=3?

## 10. What are the winning opening moves in 3 x 3, 4 x 4, and 5 x 5 Hex?

11. If the first player has to link the more distant sides of an n x (n+1) Hex board, show that the second player has a winning strategy.

12. Explain why the strategy-stealing argument of Section 2.7.2 doesn’t imply that the first player can win after playing anywhere at his first move. Beck’s Hex is the same as ordinary Hex, except that it begins with a circle in an acute corner of the board, and Cross moves first. Confirm that Cross has a winning strategy.

## 13. The game

Figure 2.20 represents the downtown street plan of a city. Players I and II represent groups of gangsters. Player I controls the areas to the north and south of the city. Player II controls the areas to the east and west. The nodes in the street plan represent street intersections. The players take turns labeling nodes that haven’t already been labeled. Player I uses a circle as his label. Player II uses a cross. A player who manages to label both ends of a street controls the street. Player I wins if he links the north and south with a route that he controls. Player II wins if she links the east and west. Why is this game entirely equivalent to Hex?

14. The game of Bridgit was invented by David Gale. It is played on a board like that shown in Figure 2.21. Black tries to link top and bottom by joining neighboring black nodes horizontally or vertically. White tries to link left and right by joining neighboring white nodes horizontally or vertically. Neither player is allowed to cross a linkage made by the other.

a. Find an argument like that used for Hex which shows that the game can’t end in a draw.

b. Why does it follow that someone can force a win?

c. Why is it the first player who has a winning strategy?

d. What is a winning strategy?

15. Two players alternately remove nodes from a connected graph G. Except in the case of the first move, a player may remove a node only if it is joined by an edge to the node removed by the previous player. The player left with no legitimate vertex to remove loses. Explain why the second player has a winning strategy if there exists a set E of edges with no endpoint in common such that each node is the endpoint of an edge in the set E. Show that no such set E exists for the graph of Figure 2.22. Find a winning strategy for the first player.

16. A strategy-stealing argument shows that if the second player to move in Tic-Tac-Toe has a winning strategy, then so does the first player. Why does it follow that the second player can’t have a winning strategy? In Hex, one can deduce that the first player has a winning strategy, but the second player can guarantee a draw in Tic-Tac-Toe. How does she guarantee a draw after the first player occupies the middle square? What is the value of Tic-Tac-Toe?

17. The value of chess is unknown. It may be W, D, or L. Explain why a simple strategy-stealing argument can’t be used to eliminate the possibility that the value of chess is L.

18. Explain why player I has a winning strategy in the number construction game of Exercise 2.12.5 when E = {x: x > 1}. What is player I’s winning strategy when E = {x: x ≥ 2}? What is player II’s winning strategy when E = {x: x > 2}? Explain why player II has a winning strategy when E is the set of all rational numbers. (A rational number is the same thing as a fraction.)

19. Let (s,t) and (s’,t’) be two different saddle points for a strictly competitive game. Prove that (s,t’) and (s’,t) are also saddle points.

20. Find all Nash equilibria in the game G of Exercise 2.12.1. Which of these are subgame perfect?

21. Find the subgame-perfect equilibria for Blackball of Exercise 2.12.3 in the case when the players’ preferences satisfy A₁ ≻ B₁ ≻ C₁ ≻ D₁; B₂ ≻ C₂ ≻ D₂ ≻ A₂; C₃ ≻ D₃ ≻ A₃ ≻ B₃. Who gets elected to the club if a subgame-perfect equilibrium is used? Find at least one Nash equilibrium that isn’t subgame perfect.

22. In the Inspection Game of Section 2.2.1, each player can choose today or tomorrow on which to act. Write down an outcome table for a five-day version of the Inspection Game in which each player can act on Monday, Tuesday, Wednesday, Thursday, or Friday. If the firm uses the mixed strategy in which each of its five pure strategies is used with equal probability, then it will win four times out of five, no matter what strategy the agency chooses. If the agency uses the same mixed strategy, show that it will win one time out of five, no matter what strategy the firm may use. Why is this pair of mixed strategies a Nash equilibrium?

23. Nothing in the surprise test paradox of Section 2.3.1 hinges on the school week having five days, and so we simplify the story by supposing that only today and tomorrow are available. As in Section 2.2, today is denoted by t and tomorrow by T. Explain why Figure 2.23 models the resulting situation as a game between Adam and Eve. (Pay close attention to the role of the information sets.) Solve the game by using backward induction. In doing so, assume that Eve will choose whatever action leaves open the possibility that she might win at her lower information set. Observe that backward induction selects a pure strategy for Adam in which he will predict that the test will be tomorrow when tomorrow comes, even though he might already have wrongly predicted that the test will be today.

24. Find the strategic form of the game of Figure 2.23. What result is obtained by deleting weakly dominated strategies?

25. In 1961, the philosopher Quine pointed out one of the logical tricks of the surprise test paradox by considering the one-day case. What was the trick he thereby exposed? Make up a similar paradox in which the evil Dr. X promises your worst possible outcome unless you act irrationally.

26. The rhyming triplets, Boris, Horace, and Maurice, are the membership committee of the very exclusive Dead Poets Society. The final item on their agenda one morning is a proposal that Alice should be admitted as a new member. No mention is made of another possible candidate called Bob, so an amendment to the final item is proposed. The amendment says that Alice’s name should be replaced by Bob’s. The rules for voting in committees call for amendments to be voted on in the reverse order to which they are proposed. The committee therefore begins by voting on whether Bob should replace Alice. If Alice wins, they then vote on whether Alice or Nobody should be made a new member. If Bob wins, they then vote on whether Bob or Nobody should be made a new member. Figure 2.24(a) is a diagrammatic representation of the order in which the voting takes place. Figure 2.24(b) shows how the three committee members rank the three possible outcomes.

Who will win the vote if everybody just votes according to their rankings? Why should Horace switch to voting for the candidate he likes least at the first vote? What happens if everybody votes strategically?

Taking Chances

## 3.1 Chance Moves

This chapter introduces chance moves into our scheme for writing down the rules of a game. This is no big deal in itself. We simply invent a mythical player called Chance, who randomizes among the actions at her decision nodes. The difficulty lies in modeling the response of rational players to the risks they face in games with chance moves. This problem is postponed until the next chapter by confining attention to win-or-lose games, in which a rational player simply maximizes the probability of winning.

3.1.1 Monty Hall Problem

This example derives from an old quiz show run by Monty Hall. His role is taken over here by the Mad Hatter to remind us that we are only looking at a toy version of the problem. He asks Alice to choose among three boxes. Two are empty, and the other contains a prize. Alice doesn’t know which contains the prize, but the Mad Hatter does.

Alice chooses Box 2. To generate some excitement, the Mad Hatter then opens one of the other boxes. When this box turns out to be empty, he invites Alice to change her mind about her choice of box. What should she do?

People usually say it doesn’t matter whether Alice changes her mind. The probability of getting the prize was one-third when she chose Box 2 because there was then an equal chance of the prize being in any of the three boxes. After one of the other boxes is shown to be empty, the probability that Box 2 contains the prize goes up to one-half because there is now an equal chance that the prize is in one of the two unopened boxes. If she switches boxes, her probability of winning will therefore still be one-half. So why bother changing?

This popular argument is wrong. It would be correct if the Mad Hatter opened boxes at random and just happened not to open a box containing the prize. But he deliberately opened an empty box. This strategic behavior conveys information to Alice. If she makes proper use of the information, she will always switch boxes. To see why, it is a good idea to represent Alice’s problem of whether to switch boxes as a game tree with a chance move. In Figure 3.2, she is player I.

The root of the game tree is a chance move, represented by a square rather than a circle. The three branches leading away from the root represent the three choices Chance can make. At this opening move, Chance can choose to put the prize in Box 1, Box 2, or Box 3. Each possibility occurs with probability 1/3. If the Mad Hatter didn’t intervene, Alice’s choice of Box 2 would therefore win the prize with probability 1/3.

The Mad Hatter is player II. He isn’t allowed to open Box 2. Nor is he allowed to open one of the other boxes if it contains the prize. He therefore has room for maneuver only if the prize is in Box 2.

Alice moves next as player I. She knows which box has been opened.

but not which of the remaining boxes contains the prize. Her knowledge at this stage is represented by two information sets, one in which she knows that Box 1 is empty, and one in which she knows that Box 3 is empty.

The doubled lines in Figure 3.2 show the actions Alice takes at each of her decision nodes if she always switches boxes. To find her overall probability of winning with this strategy, return to the original chance move. The play of the game that starts with Chance putting the prize in Box 1 ends with the outcome W. So does the play that starts with Chance putting the prize in Box 3. So the switching strategy ensures that Alice wins the prize two-thirds of the time. The other third of the time she loses because both plays that start with Chance putting the prize in Box 2 end with the outcome L. On the other hand, if she sticks with Box 2, she will win only one-third of the time.

A cleverer way to see that Alice wins with probability 2/3 by switching is to note that this is the probability that Alice would lose if the Mad Hatter didn’t intervene at all. It is therefore also the probability she will win if she switches after learning which of the other boxes is empty. But you don’t need to be clever if you let Von Neuman’s formalism do most of the thinking for you.

s S s S s S s S Alice 3 3 1 1 Alice Hatter Hatter Hatter 1 3 Chance

Figure 3.2 The Monty Hall Game. The chance move is shown as a square. Alice’s switching choice is denoted by s, and her staying choice by S. Her optimal choice of switching is indicated by doubling the appropriate branches.

## 3.2 Probability

When dice are rolled, statisticians say that the set O = {1, 2, 3, 4, 5, 6} of all possible outcomes is a sample space. Decision theorists call O the world within which their decision problems arise. The numbers 1, 2, 3, 4, 5, or 6 are then said to be the possible states of the world. The events that can result from rolling the dice are identified with the subsets of O. Thus the event that the dice shows an even number is the set E = {2, 4, 6}.

A probability measure is a function defined on the set S of all possible events.¹ The number prob(E) is said to be the probability of the event E.

To qualify as a probability measure, the function prob: S → [0, 1] must satisfy three properties. The first property is that prob(∅) = 0. Since ∅ is the set with no elements, this means that the probability of the impossible event that nothing at all will happen is zero. The second property is that prob(O) = 1, which means that the probability of the certain event that something will happen is 1.

The third property says that the probability that one or the other of two events will occur is equal to the sum of their separate probabilities—provided that the two events can’t both occur simultaneously. The set E ∩ F represents the event that both events E and F occur at the same time. So E ∩ F = ∅ means that E and F can’t occur simultaneously, as in Figure 3.3(b). The set E ∪ F represents the event that at least one of E or F occurs. So the third property can be expressed formally by writing E ∩ F = ∅ ⇒ prob(E ∪ F) = prob(E) + prob(F).

A fair die is equally likely to show any of its faces when rolled, and so prob(1) = prob(2) = · · · = prob(6) = 1/6. The probability of the event E = {2, 4, 6} that an even number will appear is therefore

¹A function f: A → B is a rule that assigns a unique b ∈ B to each a ∈ A. The object b assigned to a is denoted by f(a). It is said to be the value of the function at the point a. The notation [a, b] represents the set {x: a ≤ x ≤ b} of real numbers. The function prob: S → [0, 1] therefore assigns a unique real number x = prob(E) satisfying 0 ≤ x ≤ 1 to each event E ∈ S.

E∩ F E∩ F ̸=∅ F E E E∪ F E∪ F Ω Ω

Figure 3.3 Venn diagrams of E ∪ F.

prob(E) = prob(2) + prob(4) + prob(6) = 1/6 + 1/6 + 1/6 = 1/2.

The proper interpretation of probabilities is a subject endlessly debated by phi- losophers. For the purposes of game theory, it is usually enough to say that a statement like prob({4}) = 1/6 means that there is one chance in six of 4 being rolled.

Gamblers express the fact that prob({4}) = 1/6 by saying that the odds are 5:1 against rolling a 4. If the odds against an event occurring are a:b, then the proba- bility that the event will occur is b/(a+b).

For each dollar that you bet on a horse at odds of 5:1 against its winning, you get back five dollars if the horse wins (plus the dollar you bet). Of course, bookies wouldn’t cover their costs in the long run if they quoted the true odds against horses winning. They therefore shade the odds in their favor. You might find a bookie who offers odds of 4:1 against rolling a 4 with a fair die, but hell will freeze over before you are offered odds of 6:1!

3.2.1 Independent Events

If A and B are sets, then A × B is the set of all pairs (a, b) with a ∈ A and b ∈ B.² Figure 3.4(a) shows the sample space O² = O × O obtained when two independent rolls of the dice are observed. In this diagram, (6, 1) represents the event that 6 is rolled with the first dice, and 1 with the second. This isn’t the same event as (1, 6), which means that 1 is rolled with the first dice, and 6 with the second. The event E × F has been shaded. It is the event that 3 or more is thrown with the first dice, and 3 or less with the second dice.

There are 36 = 6 × 6 possible outcomes in the square representing O × O. If the two dice are rolled independently, each outcome is equally likely. The probability of each is therefore 1/36. So the probability of E × F must be prob(E × F) = 12/36 = 1/3.

Notice that prob(E) = 2/3 and prob(F) = 1/2. Thus, prob(E × F) = prob(E) × prob(F).

²In this context, the notation (a, b) means the pair of real numbers a and b, with a taken first. If the order of the numbers were irrelevant, one would simply use the notation {a, b} for the set containing a and b.

Second throw 1 2 3 4 5 6 E and F reinterpreted 1 (1,1) (1,2) (1,3) (1,4) (1,5) (1,6)

2 (2,1) (2,2) (2,3) (2,4) (2,5) (2,6)

First 3 (3,1) (3,2) (3,3) (3,4) (3,5) (3,6)

throw 4 (4,1) (4,2) (4,3) (4,4) (4,5) (4,6)

E E∩ F E 5 (5,1) (5,2) (5,3) (5,4) (5,5) (5,6)

6 (6,1) (6,2) (6,3) (6,4) (6,5) (6,6)

E × F (cid:6) (cid:7) (cid:6) (cid:6) (cid:7) (cid:6)

(a) (b)

Figure 3.4 The sample space O × O for two independent rolls of a die.

This equation holds whenever E and F are independent events. The conclusion is usually expressed as prob(E ∩ F) = prob(E)prob(F), which says that the probability that two independent events will both occur is the product of their separate probabilities.

Strictly speaking, writing prob(E ∩ F) = prob(E)prob(F) requires reinterpreting E and F as events in O × O as indicated in Figure 3.4(b). In this diagram, E is no longer the subset of O that represents the event that the first die will show 3, 4, 5, or 6. It is instead the subset of O × O corresponding to the event in which the first dice shows 3, 4, 5, or 6, and the second die shows anything whatever. Similarly F becomes the subset of O × O corresponding to the event that the first die shows anything whatever, and the second die shows 1, 2, or 3.

3.2.2 Paying Off a Loan Shark

To avoid getting his legs broken, Bob needs to come up with $1,000 tomorrow to pay off a loan shark. With the $2 remaining in his wallet, he therefore buys two lottery tickets for $1 each in two independent lotteries. The winner in each lottery gets a prize of $1,000 (and there are no second prizes). If the probability of winning in each lottery is q = 0.0001, what is the probability that Bob will still be walking around next week?

Let W₁ and L₁ be the events that Bob wins or loses the first lottery. Let W₂ and L₂ be the events that he wins or loses the second lottery. Then prob(W₁) = prob(W₂) = q, and prob(L₁) = prob(L₂) = 1 − q.

We need prob(W₁ ∪ W₂). This isn’t prob(W₁) + prob(W₂) because W₁ and W₂ can occur simultaneously. However, none of the events W₁ ∩ W₂, W₁ ∩ L₂, or L₁ ∩ W₂ can occur simultaneously, and so prob(W₁ ∪ W₂) = prob(W₁ ∩ W₂) + prob(W₁ ∩ L₂) + prob(L₁ ∩ W₂).

Multiplying the probabilities of the independent events on the right, we find that prob(W₁ ∪ W₂) = q² + q(1 − q) + (1 − q)q = 0.00019998. So Bob’s ambulatory prospects aren’t very good. He has less than two chances in ten thousand of coming up with the money.

It is often easier in such problems to work out the probability that the event in question won’t happen. This is the event L₁ ∩ L₂ that Bob loses both lotteries. We then get the same answer more simply as 1 − prob(L₁ ∩ L₂) = 1 − (1 − q)² = 0.00019998.

## 3.3 Conditional Probability

After an investigation into a major plane crash proved inconclusive, the New York Times carried a sequence of letters about the chances of a meteor strike. The first argued that the probability of a meteor striking an aircraft may be small, but it isn’t negligible.³ The second made fun of the first, arguing that what matters is the in- credibly smaller probability that a meteor would strike at the particular time and place of the crash. The third pointed out that the previous letters should have estimated conditional probabilities. What really matters is the probability of a meteor strike at the time and place of the crash—conditional on the crash having taken place without any other identifiable cause.

After you observe that an event F has happened, your knowledge base changes.

The only states of the world that are now possible lie in the set F. You must therefore replace O by F, which is the new world in which your future decision problems will be set. The new probability prob(E|F) you assign to an event E after learning that F has occurred is called the conditional probability of E given F.

For example, we know that prob(4) = 1/6 when a fair die is rolled. If we learn that the outcome was even, this probability must be adjusted. The event F = {2, 4, 6} that the outcome is even contains three equally likely states. The probability of rolling a 4, given that F has occurred, is therefore 1/3. Thus, prob(4|F) = 1/3.

The principle on which this calculation is based is embodied in the formula prob(E|F) = prob(E ∩ F)/prob(F).

3.3.1 Peeking in Poker

While playing poker with Bob, Alice hears a bystander whisper that he has a red queen in his hand. Would it make any difference to her estimate of the chances of his

³The letter included estimates of the rate at which meteors reach the ground and the proportion of the Earth’s surface area taken up by aircraft in flight.

holding a second queen if the bystander had identified the red queen as the queen of hearts? To answer this question, we need to compare prob (E|F) and prob (E|G), where E is the event that Bob holds two queens, F is the event that he holds the q Queen of hearts, and G is the event that he holds a red queen. To simplify the problem, suppose that Alice and Bob are playing poker with a six-card deck, two of which are dealt to each player. The cards that aren't dealt to Alice are €A, ~Q, }Q, and |8. Alice begins by conditioning on this event and deduces that Bob is equally likely to be holding any of the hands shown in Figure 3.5. There are six hands in which Bob is holding ~Q. In two of these, Bob is holding two queens. So prob(E|F) = 1. Similarly, prob(E|G) = 1, because there are two chances in ten that E will occur, given that Bob is only known to be holding a red queen.

As in the Monty Hall problem, even mathematically sophisticated people often get this wrong. They don't see why it should matter whether the red queen is the queen of hearts or not. The lesson is that big brains aren't always an asset. Instead of thinking clever thoughts, it is sometimes better simply to enumerate all the possibilities. If it is a work of great labor to do so, one can always begin with a toy version of the problem, as we did here.

3.3.2 Knowledge and Belief

If you are playing a game, your decision-theoretic world is the set of all possible plays of the game. As the game proceeds, you will usually learn more and more about which play of the game will actually be realized. Von Neumann ingeniously modeled this learning process using information sets. On reaching an information set F, you now know that the realized play of the game must pass through one of the decision nodes in F.

Game theorists distinguish what you know as a result of reaching an information set F from what you believe after reaching F. Your knowledge is determined by the rules of the game. Your beliefs are determined by your attempts to quantify the uncertainty created by the gaps in your knowledge.

Figure 3.5 Peeking in Poker.

(a) Alice's hand (b) Bob's possible hands G

The Monty Hall Game, which is shown again in Figure 3.6(a), will serve as an example. Suppose that Alice believes that the Mad Hatter will never open Box 3 when the prize is in Box 2. If she always switches boxes, Alice therefore thinks that only the plays of the game shown with doubled branches in Figure 3.6(a) are possible before the game begins. Since each play is equally likely, she starts by attaching probability prob(l) = 1 to the event that the realized play will pass through the left decision node l in her left information set L.

If the Mad Hatter opens Box 3, Alice now knows that one of the two plays of the game passing through a decision node in her left information set L has occurred. She therefore replaces the probability prob(l) = 1 by prob (l|L) = 1 because she now believes that the other play that passes through L is impossible.

Figure 3.6(b) shows a game whose rules say that Alice knows that the Mad Hatter never chooses Box 3 when the prize is in Box 2. This game obviously won't do as a vehicle for analyzing the Monty Hall problem because we wouldn't need to write a game down at all if we were so sure beforehand of what Alice believes about the Mad Hatter that we could reclassify her beliefs as knowledge.

3.3.3 Updating in the Monty Hall Game

If Alice believes that the Mad Hatter never opens Box 3 when the prize is in Box 2, then she updates her probability of being at l in Figure 3.6(a) to prob(l|L) = 1 after finding herself at the information set L. But what is the value of prob(l|L) if the Mad Hatter uses a mixed strategy in which he opens Box 1 with probability 1 - p and Box 3 with probability p?

We need to find prob(E|F) = prob(E\F)/prob(F) when E = {l} and F = L = {l,r}. Things simplify in this case because {l} is a subset of L, and so E\F = E. Thus,

prob(l|L) = prob(l) / (prob(l) + prob(r)) = (1/3) / (1/3 + p) = 1 / (1 + p).

To see that prob(r) = p * 1, we appeal again to the formula prob(E\F) = prob(E|F)prob(F), but now F is the event that the prize is in Box 2, and E is the event that the Mad Hatter opens Box 3.

Notice that it isn't true that Alice will win with probability 2 in Figure 3.1 by switching boxes. This is her probability of winning before the Mad Hatter opens a box. Without any information about the Mad Hatter's strategy, all we can say about her probability of winning after the Mad Hatter opens a box is that it lies somewhere between 1 and 1.

## 3.4 Lotteries

I never buy lottery tickets because I prefer to not to gamble when the odds are heavily stacked against me. But everybody understands how lotteries work. It therefore makes sense to use the analogy of a lottery when talking about what you might win or lose as a result of a chance move.

For example, a bookie may offer you odds of 3:4 against an even number being rolled with a fair die. If you take the bet, you win $3 if an even number appears and lose $4 if an odd number appears. Accepting this bet is equivalent to choosing the lottery L shown in Figure 3.7(a). The top row shows the possible final outcomes or prizes, and the bottom row shows the respective probabilities with which each prize is awarded.

The lottery M of Figure 3.7(b) has three prizes. You have five chances in every twelve of winning the big prize of $24.

3.4.1 Random Variables

Mathematicians talk about random variables rather than lotteries. I remember being mystified by random variables when I first studied statistics, but a kindly mathematics professor finally put me straight by explaining that a random variable is simply a function X: O → R.

For example, the lottery of Figure 3.7(a) is equivalent to the random variable X: O → R defined by

3, if o = 2, 4, or 6 X(o) = -4, if o = 1, 3, or 5.

In this case, the relevant sample space is O = {1, 2, 3, 4, 5, 6}.

If you take the bet represented by the random variable X, your probability of winning $3 is prob(X = 3) = prob({2,4,6}) = 1. Your probability of losing $4 is prob(X = -4) = prob({1,3,5}) = 1.

3.4.2 Compound Lotteries

One of the prizes in a raffle at an Irish county fair is sometimes a ticket for the Irish National Sweepstake. If you buy a raffle ticket, you are then participating in a compound lottery, in which the prizes may themselves be lotteries. It is important to remember that we always assume that all the lotteries involved in a compound lottery are independent of each other.

Figure 3.8 illustrates the compound lottery pL + (1-p)M. The notation means that you get the lottery L with probability p and the lottery M with probability 1-p. A compound lottery can always be reduced to a simple lottery by computing the total probability with which you get each prize. In the case of Figure 3.8:

q1 = p * 1/2 + (1-p) * 1/4 = 1/4 + (1/4)p, q2 = (1-p) * 5/12 = (5/12) - (5/12)p, q3 = p * 1/2 + (1-p) * 1/3 = 1/3 + (1/6)p.

To find q3, begin by noting that the probability of winning the prize L in the compound lottery is p. The probability of winning $3 in the lottery L is 1. These events are independent, and so the probability of the event E that they both occur is p * 1. Similarly, the event F that M is won in the compound lottery and that $3 is won in the lottery M has probability (1-p) * 1. Since E and F can't both happen, the event E[F that you win $3 has probability q3 = prob(E) + prob(F) = p * 1 + (1-p) * 1.

## 3.5 Expectation

The expectation or expected value EX of a random variable X is defined by

EX = Σ k prob(X = k),

where the summation extends over all values of k for which prob(X=k) isn't zero. If many independent observations of the value of X are taken, the law of large numbers says that the probability that their long-run average will differ significantly from EX is small.

Your expected dollar winnings in the lottery L of Figure 3.7 are

EL = Σ k prob(X = k)

= 3 * 1/2 + (-4) * 1/2 = -1/2.

If you bet over and over again on the roll of a fair die, winning $3 when the outcome is even and losing $4 when the outcome is odd, you are therefore likely to lose an average of about 50¢ per bet in the long run. The expected dollar value of the lottery M of Figure 3.7 is

EM = (-4) * 1/4 + 24 * 5/12 + 3 * 1/3 = 10.

If you repeatedly paid $3 for a ticket in this lottery, you would be likely to win an average of about $7 per trial in the long run.

3.5.1 The Monte Carlo Fallacy

The relation between the expected value of a random variable and its long-run average is frequently misunderstood. Figure 3.9 illustrates the relationship for the case of a fair coin. The expected number of heads in a single throw is 1. If we tossed the coin independently many times, we would be surprised if we didn't see heads appear approximately half the time.

Figure 3.9 shows the 2^7 = 128 equally likely outcomes that can result when the coin is tossed seven times. The event F consists of all outcomes in which 2, 3, 4, or 5 heads are thrown. Since we are concerned with the average number of heads thrown, observe that F is the event in which this average differs from 1/2 by less than 1/8.

There are 112 outcomes in F, and so prob(F) = 112/128 = 7/8, confirming that the average number of heads approximates its expected value of 1/2 with high probability. Many more throws would be necessary to get a probability of 0.9 that the average is within 0.1 of 1/2. Even more throws would be needed to get a probability of 0.99 that the average is within 0.01 of 1/2.

Gamblers in Monte Carlo or Las Vegas commonly attribute the law of large numbers to some mystical influence that acts to keep the average close to 1/2. When they notice that a large number of heads have been thrown, they fallaciously reason that it is more likely that a tail will be thrown next time.

It is easy to pinpoint the mistake in the Monte Carlo fallacy. Suppose that six heads are thrown with a fair coin. This is the event E in Figure 3.9. What is the probability that the next coin will be a tail? Since each toss of the coin is independent...

the total number of observations becomes infinite is equal to the expected value with probability one.

88 Chapter 3. Taking Chances

The sets are: tthhhh hhhtttt tththhh hhthttt tthhthh hhtthtt tthhhth hhtttht tthhhht hhtttth thtthhh hthhttt thththh hththtt ththhth hthttht ththhht hthttth thhtthh htthhtt thhthth htththt thhthht htthtth thhhtth httthht thhhtht httthth tthhhhh thhhhtt htttthh hhttttt ththhhh httthhh thhhttt hthtttt thhthhh htththh thhthtt htthttt thhhthh htthhth thhttht httthtt thhhhth htthhht thhttth httttht thhhhht hthtthh ththhtt httttth htthhhh hththth thththt thhtttt hththhh hththht ththtth ththttt hthhthh hthhtth thtthht thtthtt hthhhth hthhtht thtthth thtttht hthhhht hthhhtt thttthh thtttth hhtthhh hhttthh tthhtth tthhttt hhththh hhtthth tthhtht tththtt hhthhth hhttthh tthhtth tthttht thhhhhh hhthhht hhthtth tthtthh tthttth htttttt hthhhhh hhhtthh hhththt tththth ttthhtt thttttt hhthhhh hhhthth hhthhtt tthtthh ttththt ttthttt hhhthhh hhhthht hhhttth ttthhht ttthtth tttthtt hhhhthh hhhhtth hhhttht ttthhth tttthht tttthtt hhhhhth hhhhtht hhhthtt ttththh tttthth tttttht hhhhhhh hhhhhht hhhhhtt hhhhttt tttthhh ttttthh tttttth ttttttt

E F

Figure 3.9 The law of large numbers. A fair coin is tossed seven times. The set F is the event in which the average number of heads thrown differs from 1 by less than 7/32. The set E is the event that the first six tosses are heads.

Of the others, we know in advance that the answer must be 1, no matter how many heads may have already been thrown.

Alternatively, we can use Figure 3.9 to verify that prob(hhhhhh t | E) = 1. It then becomes obvious that the law of large numbers has nothing to do with the question because E lies outside the set F, within which the average number of heads is close to 1.

3.5.2 Martingales

A martingale was originally the betting system in which you double your stake after every loss. When a novice who had fallen for her charms entrusted her family diamonds to his care, Casanova thought he was going to make himself rich by playing this system in a Venetian gambling den. Like many others through the centuries, he underestimated the chances of hitting a long streak of bad luck. If Casanova had been trained in modern mathematics rather than the amatory arts, he would have known that no betting system can beat a casino's odds. Nowadays, we use the word martingale in a way that illustrates this sad fact.

Suppose, for example, that Bob uses a system when betting repeatedly on the fall of a fair coin. His wealth then varies over time according to how the coin falls. In mathematical terms, it is a sequence of random variables. Whatever Bob's system may be, this sequence is a martingale in the modern sense because, no matter what he may have won or lost up to now, his expected loss or gain on the next toss of the coin is always a big round zero.

When the idle rich return from Las Vegas boasting about paying for their vacation by using a clever roulette system, they are just fooling themselves. Even if roulette were fair, all they would have done is to trade a high probability of winning a small amount for a low probability of losing a large amount.

To see how this works, we study the most popular betting system of all. You enter a casino with a stake of $s and plan to bet $1 repeatedly that heads will be thrown with a fair coin until you have either won $w or lost your stake of $s. What is your probability of success?

If you currently have $n at some time, you are facing a lottery L_n in which your probability of eventually being successful and winning $w is p_n and your probability of eventually failing and losing $s is 1 - p_n. To find p_n, first notice that L_n is the compound lottery of Figure 3.10. Because you have half a chance of winning or losing a dollar at the next toss of the coin,

p_n = (1/2) p_{n-1} + (1/2) p_{n+1}.

Solutions to this difference equation have the form p_n = An + B, where A and B are constants. To determine A and B, use the fact that you will fail for sure when your stake is lost and succeed for sure if you hit your target amount. Thus p_0 = 0 and p_{s+w} = 1. It follows that A = 1/(s + w) and B = 0. Your probability of success when your stake is $s is therefore

p_s = s / (s + w).

If the stake you are willing to risk is large compared with your target winnings, you have a high probability of being successful. However, you don't thereby beat the odds. To see this, it is only necessary to compute your expected winnings when you start with a stake of $s:

E[L_s] = -s + w * s/(s+w) = 0.

Whatever betting system we used, this result would have been the same. It follows that casinos wouldn't make any money on average if their games were fair. Most of their games are therefore unfair. For example, you get odds of 35:1 against any particular number coming up at roulette, but there are 37 equally likely numbers (including zero). Blackjack used to be an exception, provided you were willing to delay playing until most of the cards remaining in the dealing shoe were favorable. But the management regarded such strategic play as cheating and would throw you out of the casino or worse if they caught you at it! Nowadays shuffling machines have put paid to even this small opportunity to beat the dealer.

Like Bob in Section 3.2.2, you sometimes have no alternative but to bet when the odds are unfair. The law of large numbers is then your enemy. Fooling around with betting systems does you no good at all. Instead of dividing your stake among different bets, you do best to go for the sudden-death option of betting your entire stake on a single trial.

## 3.6 Values of Games with Chance Moves

Every strictly competitive game of perfect information without chance moves has a value v (Corollary 2.1). That is, player I has a pure strategy s that guarantees him an outcome that is at least as good for him as v, while player II has a pure strategy t that guarantees her an outcome that is at least as good for her as v.

For games with chance moves, neither player will usually be able to guarantee doing at least as well as some pure outcome v every time that the game is played. If you are unlucky, you may lose no matter how cleverly you play. Even the best poker players reckon to lose one session in three.

We therefore have to cease thinking about what can be achieved for certain. A pure strategy pair only determines a lottery over the pure outcomes. Instead of asking what pure outcomes can be achieved for certain, we need to ask what lotteries can be achieved for certain. The value of a strictly competitive game with chance moves will therefore normally be a lottery.

Matters are simplified in the current chapter by confining our attention to win-or-lose games. A lottery then takes the form

W L p   1-p

A useful trick is to use the boldface notation p for the lottery in which W occurs with probability p and L occurs with probability 1 - p. For example, Figure 3.11 illustrates the fact that the compound lottery pq + (1 - p)r is equivalent to the simple lottery pq + (1 - p)r.

In win-or-lose games, a rational player will seek to maximize the probability of winning. Player I's preferences can then be described by saying that he likes the lottery p at least as much as the lottery q if and only if p >= q. The lottery p assigns player II a probability of 1 - p of winning. She therefore likes the lottery p at least as much as the lottery q if and only if p <= q. A win-or-lose game is therefore necessarily strictly competitive even if it has chance moves. That is to say,

p >= q implies p <= q.

The argument of Theorem 2.1 can now be recycled to show that we don't need to exclude chance moves when claiming that all win-or-lose games of perfect information have a value. When we have to write down the value of a subgame H whose root is a chance move, we first identify all the smaller subgames that Chance might choose at the root. The value of H is then simply the lottery that yields the values of these smaller subgames with the probabilities with which Chance chooses them.

3.6.1 Monty Hall's Value

The Monty Hall problem provides an example in which it is easy to work out the value of a win-or-lose game with a chance move.

The Mad Hatter didn't get equal billing with Alice in Section 3.1.1, but he is a player, too. In accordance with the instructions from the studio that prevent his opening Box 2 or a box containing the prize, we assume that his aim is to minimize Alice's probability of winning.

We use s to mean that Alice switches from Box 2 and S to mean that she stays with Box 2. Alice has two information sets in Figure 3.2. At her left information set she knows that Box 3 is empty. At her right information set, she knows that Box 1 is empty. At each information set she must choose between the actions s and S. (Remember that she can't choose different actions at different decision nodes in the same information set because she doesn't know which decision node in the information set has been reached when she chooses an action Section 3.1.1 shows that the entries in the first and fourth rows of the outcome table must be the lotteries 2/3 and 1/3 respectively. The same mode of reasoning also allows us to fill in the other entries in the table. For example, the pure strategy pair (sS, 3) is indicated in Figure 3.12(a) by doubling appropriate branches. To see that the outcome that results from the use of this strategy pair is 1/3, one needs only to follow the play that will result from each of the three choices Chance can make at the opening move. Two of these lead to L and the other to W. When (sS, 3) is played, Alice therefore wins the prize with probability 1/3.

Recall from Section 2.8.2 that a Nash equilibrium of a strictly competitive game occurs at a saddle point of the outcome table. To find the pure-strategy Nash equilibria of a strictly competitive game, one therefore looks for the entries in the outcome table that are best in their column and worst in their row (from player I’s point of view). At a saddle point in a strictly competitive game, each player will then be making a best reply to the other.

Figure 3.12(b) shows that the Monty Hall Game has two saddle points, (sS, 1) and (sS, 3). The entry in the outcome table at each saddle point is 2/3, and so this is the value of the game. If Alice and the Mad Hatter play optimally, Alice therefore wins the prize with probability 2/3.

Alice’s optimal strategy sS requires that she always switch from Box 2 to whichever box hasn’t been opened. As both his pure strategies are optimal, the Mad Hatter has a less exacting task. In fact, he needn’t do any thinking at all since all of his mixed strategies are optimal as well.7

7 In Section 3.3.3, we let the Mad Hatter play pure strategy 3 with probability p. This mixed strategy is optimal for him because he still gets the outcome 2/3 when Alice plays sS.

## 3.7 Waiting Games

The contestants in bicycle races sometimes behave very strategically. They start by maneuvering very slowly for position until someone suddenly breaks away in an attempt to create a decisive advantage. The waiting games of this section have a similar character. There is a waiting phase, followed by a sudden all-or-nothing winning bid by one of the players.

3.7.1 Product Races

Two firms sometimes race to be the first to get their product on the market. How long should a firm develop its product before going for broke and seeing whether its current product is good enough to grab the market? Races in which two firms try to be the first to get a new idea into a patentable form have a similar structure.

Here is a toy model of a product race between Alice and Bob. If Alice gets her product on the market first, it will be successful with probability p1. If so, she will then have such a hold on the market that Bob’s product won’t be able to get off the ground at all when marketed later. On the other hand, if Alice’s product fails when first marketed, nobody will want to buy her later attempts to improve the product. Bob can therefore take as long as he needs to come up with a product that is sure to be successful. So Bob wins with probability 1−p1 when Alice gets her product on the market first.

If Bob gets his product on the market first, he wins with probability p2, and Alice wins with probability 1−p2. We don’t need to assume much about what happens if both players market their products simultaneously, except that one will then win and the other lose.

Figure 3.13 Success probabilities: Figure 3.13(a) shows the probability of a player’s product being successful if it is first on the market at time t. Figure 3.13(b) shows the probability that a player in Duel will hit the other if he fires first when the players are d apart.

A player’s probability of winning when first on the market goes up with time. We require that p1 and p2 be continuous and strictly increasing functions of time.8 As shown in Figure 3.13(a), we also require that both functions start out at zero and eventually approach one.

We assume that Alice and Bob have already sunk the costs of developing their products and that whoever wins the market will be able to exploit it for such a long time that any losses caused by a delay in winning the market are negligible. Alice and Bob are then playing a win-or-lose game in which each seeks to maximize the probability of winning. How should they play?

If the players can monitor each other’s progress, so that we are talking about a game of perfect information with many chance moves, the solution isn’t hard to find. Rational play requires that Alice and Bob put their products on the market simultaneously as soon as

p1 + p2 = 1.

Several steps are needed to explain why:

Step 1. The solution can’t say that one player should move before the other. Alice wouldn’t follow any advice to move in advance of Bob, because she can always risklessly raise her probability of winning by cutting her lead time by a little. So both players must put their products on the market simultaneously.

Step 2. If Alice and Bob put their products on the market simultaneously when their probabilities of winning would be p1 and p2 if they moved first, then Alice will win with some probability q1. We can’t have p1 > q1 since Alice’s probability of winning by going first would decrease but still be larger than q1 if she moved a tiny bit sooner than Bob. Thus p1 ≥ q1. Since p2 ≥ q2 for similar reasons, we have that p1 + p2 ≥ q1 + q2 = 1.

Step 3. We also can’t have 1−p2 > q1 because Alice’s probability of winning by going second would remain 1−p2 if she moved later than Bob. Thus 1−p2 ≤ q1. Similarly, 1−p1 ≤ q2, and so 2−p1−p2 ≤ q1+q2 = 1. It follows that p1 + p2 ≥ 1.

Step 4. Since p1 + p2 ≤ 1 and p1 + p2 ≥ 1, it follows that p1 + p2 = 1.

This argument isn’t a proof because it takes too much for granted. But it is solid enough to explain what is going on in the more careful arguments possible in particular cases like the game of Duel, which follows.

3.7.2 Duel

Tweedledum and Tweedledee have agreed to fight a duel. Armed with dueling pistols loaded with just one bullet, they walk toward each other. The probability of either hitting the other increases the nearer the two approach. How close should

8 A real-valued function f is continuous on an interval if its graph can be drawn without lifting the pen from the paper. Actually p1 and p2 can be the realizations of a stochastic process, provided they are continuous and strictly increasing with probability one. Exercise 3.11.24 looks at a case in which p1 and p2 increase in discrete jumps at random times.

Tweedledum get to Tweedledee before firing? This is literally a question of life and death because, if he fires and misses, Tweedledee will be able to advance to point-blank range with fatal consequences for Tweedledum.

One way of modeling the problem is shown in Figure 3.14. The initial distance between the players is D. Points d0, d1, ..., dn have then been chosen with 0 = d0 < d1 < ... < dn = D to serve as decision nodes in the finite game of Figure 3.15(a). We assume that the distance between each pair of neighboring points is very small with a view to taking the limit as n → ∞ at the end of the analysis.

In Figure 3.15(a), Tweedledum is player I and Tweedledee is player II. Thus W means that Tweedledum lives and Tweedledee dies. Similarly, L means that Tweedledee lives and Tweedledum dies.

The square nodes are chance moves. At these nodes, Chance determines whether a player will hit or miss his opponent after firing his pistol. Figure 3.13(b) shows the probability p_i(d) that player i will hit his target when he fires from distance d. We assume that p_i is continuous and strictly decreasing on [0, D], with p_i(0)=1 and p_i(D)=0.9 Differences in the hitting probabilities between the two players reflect their differing skills with a dueling pistol.

Solving the game. All finite win-or-lose games of perfect information have a value v. Since v is a lottery in this case, player I has a strategy s that guarantees his survival with probability v or more. Player II has a strategy t that guarantees his survival with probability 1−v or more. We use backward induction to determine these optimal strategies.

Step 1. First look at the smallest subgames in Figure 3.15(a). These are all no-player games rooted at a chance move reached after someone fires his pistol. If player I survives in such a subgame with probability p, then the value of the subgame is simply the lottery p. Each subgame may therefore be replaced with a leaf labeled with the symbol p. This first step in the backward induction process has been carried through in the reduced game of Figure 3.15(b).

9 The function is decreasing rather than increasing as in Section 3.7.1 because it is now a function of distance rather than time.

Step 2. If we ignore the subgame rooted at d0, where player II’s only choice is to fire, the smallest subgame in Figure 3.15(b) is rooted at d1. Player I has a choice between firing and waiting at this node. Firing leads to the lottery p1(d1). Waiting leads to the lottery 1−p2(d0). He therefore fires if

p1(d1) > 1−p2(d0), p1(d1) + p2(d0) > 1.

This inequality holds because our assumptions make p1(d1) + p2(d0) nearly equal to 2. So player I will fire at node d1. The branch that represents this choice has therefore been doubled in Figure 3.15(b).

Step 3. It is optimal for player II to fire at node d2 if

1−p2(d2) < p1(d1), p1(d1) + p2(d2) > 1.

This inequality holds because p1(d1) + p2(d2) is only slightly less than p1(d1) + p2(d0). So player II will fire at node d2. The branch that represents his choice has therefore been doubled in Figure 3.15(b).

n doubled in Figure 3.15(b).

Step 4. All the firing branches get doubled in this way until the first time that neighboring nodes c and d are reached for which p₁(d) + p₂(c) ≤ 1.

This must happen eventually because p₁(dₙ) + p₂(dₙ₋₁) is nearly 0.

Step 5. From now on, only the case when c < d and p₁(d) + p₂(c) < 1 illustrated in Figure 3.15(b) will be considered in detail. In this case, the waiting branch at node d must be doubled because 1 - p₂(c) > p₁(d), and so it is optimal for player I to wait at node d.

Step 6. The waiting branch has also been doubled at the smallest node e larger than d. It is optimal for player II to wait at node e because firing leads to the lottery 1 - p₂(e), in which he survives with probability p₂(e), whereas waiting leads to the lottery 1 - p₂(c), in which he survives with probability p₂(c). He prefers the latter because p₂(c) > p₂(e).

Step 7. All the waiting branches get doubled in this way whenever the players are more than d apart. If they play optimally, both players will therefore plan to wait until they are distance d apart and to fire thereafter at the earliest opportunity.

Step 8. Since c and d are the first pair of neighboring nodes for which p₁(d) + p₂(c) ≤ 1, it must be true that p₁(b) + p₂(c) > 1. But the functions p₁ and p₂ are continuous, and we have assumed that the points b, c, and d are all close to each other. It follows that all three points must also be close to the point d at which p₁(d) + p₂(d) = 1.

Conclusion. Backward induction selects a pure strategy for each player that consists of waiting until the opponent is approximately d away and then planning to fire at all subsequent opportunities. The value of the game is approximately v, where v = p₁(d) = 1 - p₂(d). If the players use their optimal strategies, Tweedledum will therefore survive with probability about v, and Tweedledee will survive with probability about 1 - v.

The closer together we place the decision nodes, the better the approximations become in this analysis. In the limiting case as n → ∞, we recover the conclusion of our product race example.

In the case when p₁(d) = 1 - d/D and p₂(d) = 1 - (d/D)², the players should wait until they are d apart, where d/D + (d/D)² = 1.

The positive root of this quadratic equation is d/D = (√5 - 1)/2. So nothing will happen until Tweedledum and Tweedledee are about 61% of their original distance apart, when each will fire simultaneously. Tweedledee will be more likely to survive because the probability of his hitting Tweedledum at a given distance is always greater than the probability of Tweedledum hitting him.

## 3.8 Parcheesi

When visiting India, I was taken to a palace of the Grand Mogul to see the giant fun marble board on which Akbar the Great played Parcheesi using beautiful maidens as pieces.¹⁰ Parcheesi (or Ludo) is still popular, ranking third after Monopoly and Scrabble on the best-seller list of board games, but the box you buy at the mall contains no beautiful maidens. All you get is a folding board like that in Figure 3.16(a), sixteen counters, and two dice. The toy version to be studied here is even less exotic. It is played on the simplified board of Figure 3.16(b) with just two counters and a fair coin.

Parcheesi is an infinite game in that the rules allow it to continue forever. However, such an eventuality occurs with zero probability and so is irrelevant to an analysis of the game.¹¹ In any case, this and other technical issues will be ignored. We will simply take for granted that our toy version of Parcheesi and all its subgames have values and focus on determining what these values are.

3.8.1 Simplified Parcheesi

Simplified Parcheesi is played between White and Black on the board shown in Figure 3.16(b). The winner is the first to reach the shaded square following the routes indicated. The players take turns, starting with White. The active player either moves his or her counter or leaves it where it is.¹²

If the counter is moved, it must be moved one square if tails is thrown with a toss of a fair coin. If heads is thrown, the counter must be moved two squares. The last rule has an exception: if the winning square can be reached in one move, the winning move is allowed even when heads has been thrown.

What makes Parcheesi fun to play is the final rule. If a player’s counter lands on top of the opponent’s counter, then the opponent’s counter is sent back to its starting place.

¹⁰ Instead of dice, he threw six cowrie shells. If all six shells landed with their open part upward, one could move a piece twenty-five squares—hence parcheesi, which is derived from the Hindi word for twenty-five.

¹¹ A zero probability event needn’t be impossible. If a fair coin is tossed an infinite number of times, it is possible that the result might always be tails, but this event has zero probability.

¹² If both players choose never to move their counters from some point on, the game is a standoff. The winner is then determined simply by tossing the coin.

Figure 3.16 Boards for Parcheesi.

3.8.2 Possible Positions in Simplified Parcheesi

The eight possible positions that White might face when it is his turn to move are listed in Figure 3.17. The value corresponding to each position is written beneath it. Positions 1 and 2 therefore have the lottery 1 written beneath them because White can win for certain if these positions are reached when it is his turn to move.

The eight positions that Black might face when it is her turn to move are listed in Figure 3.18. Their values can be determined from Figure 3.17. For example, position 11 looks the same to Black as position 3 looks to White. Since position 3 has value a, the value for position 11 must therefore be 1 - a.

The value for simplified Parcheesi is f since the game starts in this position with White to move. But we can’t work out f by backward induction without also determining the values of a through e along the way.

3.8.3 Solving Simplified Parcheesi

We will again use backward induction to solve the game, but this time we have to work harder than usual.

Step 1. The subgame rooted at position 3 in Figure 3.19 shows the optimal actions for White after the coin is tossed. Thus a = ½·1 + ½·(1 - d), and so a = ½(1) + ½(1 - d)

a + d/2 = 1. (3.1)

Step 2. Position 6 in Figure 3.19 can be treated in the same way. Thus, d = ½(1 - d) + ½(0)

d = 1/3 a = 5/6 (by equation 3.1)

Step 3. It isn’t immediately obvious whether White should move his counter after throwing a tail in position 4 of Figure 3.19. If 1 - b ≥ ½ (and so b ≤ ½), it would be optimal for White to move. But then b = ½(1) + ½(1 - a)

= ½(1) + ½(1/6)

b = 7/12, which is a contradiction. So it is optimal not to move, and b = ½(1) + ½(1 - b)

b = 2/3.

Step 4. We take positions 5 and 7 in Figure 3.19 together. If 1 - e ≤ ½ (and so e ≥ ½), an examination of position 5 shows that c = ½(1) + ½(1 - e)

c + e/2 = 1. (3.2)

But then 1 - c = e/2 ≥ ¼, and so, from position 7, e = ½(1 - a) + ½(1 - b)

= ½(1/6) + ½(1/3)

e = 1/4 (3.3)

c = 7/8 (by equation 3.2) (3.4)

Equations (3.3) and (3.4) were obtained on the assumption that e ≥ ½. But it may be that e < ½. If so, position 5 tells us that c = ½(1) + ½(1 - d)

= ½(1) + ½(2/3) = 5/6, and so, from position 7, e = ½(1) + ½(1) = 1, which contradicts the hypothesis that e < ½. So equations (3.3) and (3.4) do in fact hold.

Step 5. If f < ½, White would steal Black’s optimal strategy by refusing to move at his first turn, whatever the coin toss showed. It follows that f ≥ ½, and so 1 - f ≤ ½. We can therefore deduce from position 8 that f = ½(1 - d) + ½(1 - e)

= ½(2/3) + ½(3/4)

f = 17/24.

Conclusion. White can guarantee winning simplified Parcheesi with a probability of at least 17/24. He should always move his counter unless a tail is thrown in positions 4, 5, or 6. In positions 4 and 5 he shouldn’t move his counter if a tail is thrown. In position 6, his decision doesn’t matter. Black’s optimal strategy is a mirror image of White’s. With this strategy, she guarantees winning with a probability of at least 7/24. The value of the game is the lottery 17/24.

## 3.9 Roundup

This chapter is about chance moves, at which a mythical player called Chance makes choices according to a predetermined probability measure. The Monty Hall problem shows that paradoxes can easily be avoided by adopting a systematic modeling methodology.

A probability measure assigns a real number prob(E) between 0 and 1 to each event E. The probability that one of two events E and F will occur when both can’t occur simultaneously is prob(E) + prob(F). The probability that both of two independent events E and F will occur is prob(E)·prob(F). We need conditional probabilities when E and F aren’t independent. A conditional probability prob(E|F) gives the probability that E will occur, given that F has already occurred.

A random variable can be thought of as a lottery ticket. The prizes in some lotteries are tickets for other lotteries. Any such compound lottery can be reduced to a simple lottery using the laws for combining probabilities. When the prizes are given in numerical terms, one can compute the expected value EL of a lottery L. It is equal to the sum of the values of each prize weighted by the probability of winning the prize. If you repeatedly participate in the lottery, your average winnings will be close to EL with high probability in the long run.

Win-or-lose games are necessarily strictly competitive even if they have chance moves.

The value p of such a game is a lottery in which player I wins with probability p and player II wins with probability 1-p.

The classical waiting game is called Duel. Economic games in which the players race to be the first to patent an idea or to get a product on the market have the same basic structure. A backward induction analysis shows that both players act when their probabilities of winning sum to one. The intuition is that you should act immediately before your opponent unless you are more likely to win by letting him shoot first.

## 3.10 Further Reading

How to Gamble If You Must, by Lester Dubbins and Leonard Savage: McGraw-Hill, New York, 1965. This is a mathematical classic.

Theory of Gambling and Statistical Logic, by Richard Epstein: Academic Press, New York, 1967. This book is more fun than the book by Dubbins and Savage and fits better into a game theory context, but it still requires some mathematical sophistication.

Introduction to Probability Theory, by William Feller: Wiley, New York, 1968. The first volume is a wonderful general introduction to probability theory, but you still need to know some mathematics.

New Games Treasury, by Merilyn Mohr: Houghton Mifflin, New York, 1997. How to play an enormous number of games for fun.

Beat the Dealer, by Edward Thorp: Blaisdell, New York, 1962. A statistician explains how he beat the dealer at blackjack.

## 3.11 Exercises

1.  Marilyn Vos Savant used to write a column in Parade magazine based on her reputation of having the highest IQ ever recorded. Various mathematical gurus laughed her to scorn when she answered a question about the Monty Hall problem by saying that switching is always optimal. In reply, she observed that switching would obviously be right if 98 boxes out of 100 were opened. Why is the answer obvious in this case?

2.  Martin Gardner used his column in Scientific American to get in on the Monty Hall act. He observed that Monty Hall might choose to open a box only when the contestant would lose by switching. Without getting formal, replace the game of Section 3.1.1 by another game in which the Mad Hatter has the option of not opening a box at all. Why is always switching no longer an equilibrium strategy for Alice?

## 3.  Explain why the number of distinct hands in straight poker is

(52 choose 5) = 52!/(5!47!) = (52*51*50*49*48)/(5*4*3*2*1).

(A deck of cards contains 52 cards. A straight poker hand contains 5 cards. You are therefore asked how many ways there are of selecting 5 cards from 52 cards when the order in which they are selected is irrelevant.)

What is the probability of being dealt a royal flush in straight poker? (A royal flush consists of the A, K, Q, J, and 10 of the same suit.)

4.  You are dealt ♠A, K, Q, 10 and ♥2. In draw poker, you get to change some of your cards after the first round of betting. If you discard the ♥2, hoping to draw the ♠J, what is the probability that you will be successful? What is the probability of drawing a straight?¹³ (Any J will suffice for this purpose.)

5.  Bob is prepared to make a bet that Punter’s Folly will win the first race when the odds are 2:1 against. He is prepared to make a bet that Gambler’s Ruin will win the second race when the odds are 3:1 against. He isn’t prepared to bet that both horses will win when the odds for this event offered are 15:1 against. If the two races are independent, is Bob consistent in his betting behavior?

## 6.  Find the expected value in dollars of the compound lottery:

$3   $2   $2   $12   $3 1    1    1    1     1 -    -    -    -     - 2    2    2    6     3 1    2 -    - 3    3

7.  The game of Figure 3.20 has only chance moves that represent independent tosses of a fair coin. Express the situation as a simple lottery. How does your representation change when the chance moves are not independent but all refer to a single toss of the same coin?

8.  The following table shows the probabilities of the four pairs (a,c), (a,d), (b,c), and (b,d):

c       d a   0.01    0.09 b   0       0.9

The random variable x can take either of the values a or b. The random variable y can take either of the values c or d. Find: a. prob (x = a)

b. prob (y = c)

c. prob (x = a and y = c)

d. prob (x = a or y = c)

9.  In a faraway land long ago, boys were valued more than girls. So couples kept having babies until they had a boy. The frequency of boys and girls in the population as a whole remained equal, but what was the expected frequency of girls per family?¹⁴ (Assume that each sex is equally likely.)

10. Alice learns that the first card dealt to Bob is a red queen in the problem of Section 3.3.1. What is her probability that Bob is holding a pair of queens? How would this probability change if she had seen that his first card was the queen of hearts?

11. Alice is dealt ♦A and ♣7 from the deck of Figure 3.4. What is her probability that Bob has a pair of queens if she learns that he has a red queen in his hand? How would this probability change if she had learned that the red queen was the queen of hearts?

12. Bob is the proud father of two children, one of whom is a girl. What is the probability that the other child is a girl? What would the probability have been if you knew that his older child were a girl?

13. Suppose that Casanova bets one Venetian sequin on the fall of a fair coin and keeps doubling up his stake until he wins. If he wins for the first time on the nth toss of the coin, show that he will win precisely one sequin overall. How many sequins will he need to have started with to carry out this strategy when n = 20?

14. As long as Casanova has any money in his pocket, he always bets $1 on the fall of a fair coin until he runs out of money or succeeds in winning a total of $1. When he loses, he doubles his previous stake. If he begins with $31 and always bets on heads to win, explain why he will succeed in his aim with any of the sequences that begin H, TH, TTH, TTTH, or TTTTH but fail with any sequence that begins TTTTT. What lottery does he face? Why is its expected dollar value zero?

15. The coin tossed in Section 3.5.2 is no longer fair. It lands heads with probability q, and the odds are now m : 1 against a head. Show that p_{n+1} = q * p_n + (1 - q) * p_{n+m+1}.

If r = (1 - q)/q, deduce that the probability of success is p_s = (1 - r^s) / (1 - r^{s+w}).

16. Player I can choose l or r at the first move in a game G. If he chooses l, a chance move selects L with probability p or R with probability 1-p. If L is chosen, the game ends in the outcome L. If R is chosen, a subgame identical in structure to G is played. If player I chooses r, then a chance move selects L with probability q or R with probability 1-q. If L is chosen, the game ends in the outcome W. If R is chosen, a subgame is played that is identical to G except that the outcomes W and L are interchanged together with the roles of players I and II.

a. Begin the game tree.

b. Why is this an infinite game?

c. With what probability will the game continue forever if player I always chooses l?

d. If the value of G is v, show that v = q + (1-q)(1-v) and work out the probability v that player I will win if both players use optimal strategies.

e. What is v when q = 1?

17. Analyze Nim when the players don’t alternate in moving but always toss a fair coin to decide who moves next.

18. In the product race of Section 3.7.1, the probability that a player will win if he or she puts their product on the market after t days is p(t) = 1 - e^{-t/100}.

Show that both will market their products after 69.3 days.

19. In the product race of Section 3.7.1, why is there a unique time at which p₁ + p₂ = 1? What implicit assumption about the probabilities that Alice and Bob will win at this time is made in the text in order to ensure the existence of a solution?

20. How close to the opponent before firing should one get in Duel when p₁(d) = p₂(d) = 1 - (d/D)²?

21. The analysis of Duel of Section 3.7.2 looks in detail only at the case when c < d and p₁(d) + p₂(c) < 1. How do things change if p₁(c) + p₂(d) < 1? What happens when c < d and p₁(d) + p₂(c) = 1?

22. How does the analysis of Duel change if p₁(D) + p₂(D) > 1? What if p₁(0) + p₂(0) < 1? What if p₁(d) + p₂(d) = 1 for all d satisfying ⅓D ≤ d ≤ ⅔D?

23. How does the analysis of Duel change if extra nodes are introduced between d_k and d_{k+1}, all of which are assigned to the player who decides at node d_k?

24. What does optimal play look like in Duel if the player who gets to fire at any node is decided by a chance move that assigns equal probabilities to both players?

25. We return to the product race game of Section 3.7.1 to consider a version in which the probabilities p₁ and p₂ progress in a sequence of discrete jumps determined by Chance.

At random times, Chance picks either Alice or Bob with equal probability and increments his or her current value of p by 1 until p₁ = 1, p₂ = 1, or a player has stopped the game by putting their product on the market. Begin to draw a game tree in which chance moves represent some player getting an increment. After such a chance move, assume that the player who gets an increment moves first and the other player moves second. Forget about the random times at which these chance moves occur. Draw enough of the game tree to allow a backward induction analysis.¹⁵ Show that it is always optimal for either Alice or Bob to go to the market when p₁ + p₂ = 1.

26. What is the probability that the simplified Parcheesi of Section 3.8.1 will continue for five moves or more if both players always move their counters the maximum number of squares consistent with the rules?

27. What is the strategy-stealing argument appealed to at Step 5 in Section 3.8.3 during the analysis of simplified Parcheesi? What strategy-stealing argument shortens the argument at Step 3?

28. No mention is made in Section 3.8.3 of the possibility that neither player may choose to move at all on consecutive turns. Why does this possibility not affect the analysis?

29. Analyze the simplified Parcheesi game of Section 3.8.1 with the modification that, when a head is thrown, a player may move 0, 1, or 2 squares at his or her discretion. Assume that the other rules remain unchanged.

d. 30. Analyze the simplified Parcheesi game of Section 3.8.1 with the modification that, when a counter is exactly one square from the winning square, then only the throw of a tail permits it to be advanced. Assume that the other rules remain unchanged.

31. When a “roulette wheel” from Figure 3.21 is spun, each number on it is equally likely to result. In Gale’s Roulette, player I begins by choosing a wheel and spinning it. While player I’s wheel is still spinning, player II chooses one of the remaining wheels and spins it. The player whose wheel stops on the larger number wins, and the other player loses.

a. If player I chooses wheel 1 and player II chooses wheel 2, the result is a lottery p. What is the value of p? (Assume that the wheels are independent.)

b. Draw an extensive form for Gale’s Roulette.

c. Reduce the game tree to one without chance moves, as was done for Duel in Section 3.7.2.

d. Show that the value of the game is 4/9, so that player II wins more often than player I when both play optimally.

e. A superficial analysis of Gale’s Roulette would suggest that player I should choose the best wheel. Player II will then have to be content with the second-best wheel. But this can’t be right because player I would then win more often than player II. What is the fallacy in the argument?

32. Let O = {1, 2, 3, ..., 9}. If player I chooses wheel 2 in Gale’s Roulette of the previous exercise, he is selecting a lottery L with prizes in O. Express this lottery as a table of the type given in Figure 3.6. Show that E(L1) = E(L2) = E(L3) = 5. Let L1 ⊗ L2 denote the lottery in which the winning prize is o1 ⊗ o2 if the outcome of lottery L1 is o1 and the outcome of lottery L2 is o2. What is the probability of the prize 2 ⊗ 4 = 6 in the lottery L1 ⊗ L2? Why is it true that E(L1 ⊗ L2) = E(L1) ⊗ E(L2)? Deduce that E(L1 ⊗ L2) = E(L2 ⊗ L3) = E(L1 ⊗ L3) = 0.

33. In an alternative version of Gale’s Roulette, each of the three roulette wheels is labeled with four equally likely numbers. The numbers on the first wheel are 2, 4, 6, and 9; those on the second wheel are 1, 5, 6, and 8; and those on the third wheel are 3, 4, 5, and 7. If the two wheels chosen by the players stop on the same number, the wheels are spun again and again until someone is a clear winner.

a. If player I chooses the first wheel and player II chooses the second wheel, show that the probability p that player I will win satisfies p = 1/2 + (1/16)p.

b. What is the probability that player I will win the whole game if both players choose optimally?

34. This exercise is for bridge fiends. West is declarer in three no trumps for the deal of Figure 3.22. To keep things simple, assume that she somehow knows that the diamond suit is equally split between her opponents. After a spade lead, West sees that she can win for sure if she can make at least one trick from two finesses in hearts and diamonds. Experts advise taking both finesses in diamonds.

a. By examining all combinations of cards that North and South might hold, show that the probability that the first diamond finesse succeeds is 1/2. The probability that either North or South holds ♦K is 1/2. The same goes for ♦Q. So why isn’t the answer 1 = 1/2 + 1/2? Why would the answer be nearly 1 if there were a hundred cards per suit?

b. Show that West’s probability of winning at least one trick from two diamond finesses is 2/3. Show that West’s probability of winning at least one trick from one diamond finesse and one heart finesse is 5/8.

c. Show that the probability of winning a second diamond finesse after losing the first is 2/3. Show that the probability of winning a heart finesse after losing a diamond finesse is 3/4.

d. Experts appeal to the preceding fact when justifying their advice to take both finesses in diamonds, but they usually say that the probability of winning a second diamond finesse after losing the first is 1/2. Why would they be about right if there were a hundred cards per suit?

e. In actual play, the relevant probability after losing the first diamond finesse needs to be conditioned on whether the finesse loses to ♦K or ♦Q. Show that this probability can vary between 2/3 and 1, depending on the probabilities with which South plays ♦K or ♦Q when holding ♦K Q.

f. In the subgame that follows West’s losing the first diamond finesse, explain why it is a strongly dominated strategy for West to take the heart finesse.

35. If all the players in a game become better informed, they may suffer. Confirm this observation by studying a game in which Adam and Eve each choose dove or hawk without observing the roll of a fair die. Unless a six is rolled, a player who chose dove receives a payoff of 1, and a player who chose hawk receives a payoff of 0. If a six is rolled, the payoffs are determined by the payoff table for the Prisoners’ Dilemma given in Figure 1.3(a). Show that the players get a smaller expected payoff if the roll of the dice becomes common knowledge before they choose.

36. Lyle Stuart was a big-time gambler who wrote a book on how to win at baccarat and craps. For example, always go to Las Vegas by yourself—you aren’t there for fun and games! This exercise is sacred to the memory of Mannie Kemmel, who would apparently wait patiently at the dice table until a number didn’t show up for 40 rolls or so and then begin to bet that number every roll. If it failed to come up in another 30 rolls, he would increase his bet. We are told that Mannie rarely failed to walk away with a profit. The story could well be true. If so, does it imply that Mannie found a way around the martingale theorem? (Section 3.5.2)

37. Another of Lyle Stuart’s stories concerns a gambler whose son became a mathematician. When the son explains that there is no way to beat the dealer, his father asks where he thinks the money came from to pay for his college education. How should the son reply?

## 4.1 Payoffs

In explaining how risk and time enter into the rules of a game, the previous two chapters made no appeal to the theory of utility. But the time has now come to provide a proper account of the way that game theorists use payoffs to model how the players of a game choose between the alternatives available to them.

Chapter 1 explains why it is important to be careful when introducing payoffs. Popular accounts of game theory often try to short-circuit the necessary explanations by simply saying that payoffs are sums of money. This creates no problem if the players are actually trying to make as much money for themselves on average as they can. But game theorists don’t restrict themselves to saying what is rational for money grubbers. Our results apply to all rational players, however they are motivated. It follows that payoffs can’t be measured just in dollars. In the general case, they are measured in units of utility called utils.

To speak of utility is to raise the ghost of a dead theory. Victorian economists thought of utility as measuring how much pleasure or pain a person feels. Nobody doubts that our feelings influence the decisions we make, but the time has long gone when anybody thought that a simple model of a mental utility generator is capable of capturing the complex mental process that swings into action when a human being makes a choice. The modern theory of utility has therefore abandoned the idea that a util can be interpreted as one unit more or less of pleasure or pain.

One of these days, psychologists will doubtless come up with a workable theory of what goes on in our brains when we decide something. In the interim, economists get by with no theory at all of why people choose one thing rather than another. The modern theory of utility makes no attempt to explain choice behavior. It assumes that we already know what people choose in some situations and uses this data to deduce what they will choose in others—on the assumption that their behavior is consistent.

In game theory, we take as our data the choices that the players would make when solving one-person decision problems by themselves and seek to deduce the choices that they will make when they play games together.

## 4.2 Revealed Preference

Students of economics usually first meet utility theory when modeling the behavior of consumers. Pandora buys a bundle of goods on each of her weekly visits to the supermarket. Since her household budget and the supermarket prices vary from week to week, the bundle she purchases isn’t always the same. However, after observing her shopping behavior for some time, it becomes possible to make an educated guess about what she will buy next week, once one knows what the prices will be and how much she will have to spend.

In making such inferences, two assumptions are implicitly understood. The first is that Pandora’s choice behavior is stable. We obviously won’t be able to predict what she will buy next week if something happens today that makes our data irrelevant. If Pandora loses her heart to a football star, who knows how this might affect her shopping behavior? Perhaps she will buy no pizza at all and instead fill her basket with deodorant.

Pandora’s choice behavior must also be consistent. We certainly won’t be able to predict what she will do next if she just picks items off the shelf at random, whether or not they are good value, or satisfy her needs. But what are the criteria that determine whether her behavior is consistent or not? This chapter is largely devoted to the manner in which this question is answered by modern utility theory.

4.2.1 Money Pumps The following example illustrates the kind of way in which economists justify the consistency assumptions they attribute to rational players.

Adam has an apple. Eve offers to exchange his apple for a fig plus a penny. Adam agrees, and now he has a fig. Eve next offers to exchange his fig for a lemon plus a penny. Adam agrees, and now he has a lemon. Eve now offers to exchange his lemon for an apple plus a penny. Adam agrees, and so he ends up with the apple with which he started—minus three cents.

pennies that are now in Eve's purse.

If Adam's choice behavior is stable, Eve can now repeat the cycle over and over again until she has extracted every cent he has. A rational player obviously wouldn't fall victim to such a money pump. What do we have to assume about Adam's choice behavior to eliminate the possibility that he might?

Economists say that the choices that Adam makes reveal his preferences. If he trades an apple for a fig plus a penny, he reveals a strict preference for a fig over an apple. As in Section 2.2, we then write apple ≺ fig. This notation allows us to summarize his revealed choice behavior as: apple ≺ fig ≺ lemon ≺ apple.

It is then evident that Adam fell victim to Eve's money pump because his revealed preferences go around in a circle. Eliminating such cycling from a rational player's choice behavior is therefore our first priority.

4.2.2 Full and Consistent Preferences The crudest way to specify the preferences revealed by a player's choices is to use a preference relation ≿. We assume that a rational player will reveal preferences that satisfy the following criteria: a ≿ b or b ≿ a (totality)

a ≿ b and b ≿ c ⇒ a ≿ c (transitivity)

for all a, b, and c in the set O of all possible outcomes.

The transitivity that prevents cycling is the only genuine consistency requirement. Totality merely says that the player is always able to express a preference between any two outcomes.¹ A preference relation ≿ shouldn't be confused with the relation ≥ used to indicate which of two numbers is larger. The latter satisfies an extra condition: a ≥ b and b ≥ a ⇒ a = b, which we certainly don't want all preference relations to satisfy. Instead of making this assumption, we define the indifference relation ∼ by: a ≿ b and b ≿ a ⇔ a ∼ b.

The strict preference relation ≺ is defined by: a ≿ b and not(a ∼ b) ⇔ a ≺ b.

## 4.3 Utility Functions

In making a rational decision, Pandora faces two tasks. The first is to identify the feasible set—the subset S of O consisting of those outcomes that are currently available. The second task is to find an optimal outcome in S. This is an outcome in S that she likes at least as much as any other outcome in S.

The problem of finding an optimal o looks easy when stated in this abstract way, but it can be hard to solve in practice if O is a complicated set, and so Pandora's preference relation ≿ is difficult to describe.

¹ In mathematics, a relation satisfying totality and transitivity is a pre-ordering. If totality is replaced by a ≿ a (reflexivity), then ≿ becomes a partial pre-ordering.

Utility functions are a mathematical device introduced to simplify the optimization problem. A preference relation ≿ is represented by such a utility function u: O → R if and only if u(a) ≥ u(b) ⇔ a ≿ b.

Finding an optimal o then reduces to solving the maximization problem: u(o) = max u(s), s∈S for which many mathematical techniques are available. A maximizing o may not exist if S is an infinite set, but we won't need to worry much about such technical difficulties. Nor is there any need to get hung up about the fact that there may sometimes be more than one maximizing o.

4.3.1 Optimizing Consumption Pandora likes to drink martinis before dinner. It isn't good for her health, but in spite of the title of this chapter, there is no accounting for tastes. Philosophers sometimes say that one consistent set of preferences can be more rational than another, but Section 1.4.1 explains why economists don't join them in telling people what they ought to like. For us, Pandora's preference relation ≿ is part of what makes her a person, like the length of her nose or the color of her hair.

Pandora regards gin and vodka as perfect substitutes for making martinis. This means that she is always willing to exchange one for the other at a fixed rate. In this example, she is always willing to trade at a rate of three bottles of gin for four bottles of vodka.

Let O be the set of all commodity bundles (g, v) consisting of g bottles of gin and v bottles of vodka. The choices Pandora makes when deciding between bundles in O can be expressed in terms of a revealed preference relation ≿, whose structure is indicated in Figure 4.1 by drawing its indifference curves, together with little arrows that show which indifference curves she prefers.² The simplest utility function U : O → R that represents Pandora's preference relation is given by U(g, v) = 4g + 3v.

For example, the fact that she is indifferent between the commodity bundles (3,0) and (0,4) is reflected in the fact that U(3,0) = U(0,4) = 12.

Pandora can buy vodka at $10 a bottle and gin at $15 a bottle. If she has $60 to spend on feeding her martini habit, how will she split the money between gin and vodka?

If we ignore the fact that liquor stores usually sell their merchandise only in whole numbers of bottles, Pandora's feasible set S consists of all bundles (g, v) with g ≥ 0 and v ≥ 0 that lie on or below her budget line: 10g + 15v = 60. We need to find her optimal bundle in this feasible set. This is a very simple example of a linear programming problem, in which a linear function must be maximized subject to a set of linear inequalities (Section 7.6).

Assuming that any money she doesn't spend is wasted, her optimal bundle o = (g, v) lies on her budget line. Her utility at this bundle is therefore U(g, 4 – 2g/3) = 4g + 3(4 – 2g/3) = 12 + 2g/3, which is largest when g is biggest. She therefore buys no vodka at all. Since her $60 will buy six bottles of gin, her optimal bundle is o = (6,0).

Figure 4.1 illustrates the solution. Pandora's indifference curves correspond to contours of her utility function. Just as the height of a hill is constant along a contour on a map, so Pandora's utility is constant along a contour like U = 12. Contours like U = 36 that don't have a point in common with the feasible set S correspond to unattainable utility levels. The contour with the highest utility that intersects with S is U = 24. Its unique point of intersection with S is o = (6,0), which is Pandora's optimal bundle.

² An indifference set for ≿ consists of all s ∈ O that satisfy s ∼ o for some given o. Such a set is usually a curve in economics examples.

4.3.2 Constructing Utility Functions Pandora's choice behavior reveals that she has consistent preferences over the six commodity bundles a, b, c, d, e, and f. Her preferences are a ≺ b ∼ c ≺ d ≺ e ∼ f.

Thus, if Pandora's feasible set is {a, b, c}, she won't choose a, but she might choose either b or c. If her feasible set is {b, c, d}, then only d is optimal.

x a b c d e f U (x) 0 1/2 1/2 3/4 1 1 V (x) –123 18 18 19 2,947 2,947 Figure 4.2 Constructing utility functions. The method always works for a consistent preference relation defined over a finite set of outcomes, because there is always another real number between any pair of real numbers.

It is easy to find a utility function U: {a, b, c, d, e, f} → R that represents Pandora's preferences. She regards the bundles a and f as the worst and the best available. We therefore set U(a) = 0 and U(f) = 1. Since she is indifferent between e and f, we must also set U(e) = 1. Next pick any bundle intermediate between the worst bundle and the best bundle, and take its utility to be 1/2. In Pandora's case, b is a bundle intermediate between a and f, and so we set U(b) = 1/2. Since b ∼ c, we must also set U(c) = 1/2. Only the bundle d remains. This is intermediate between c and e, and so we set U(d) = 3/4 because 3/4 is intermediate between U(c) = 1/2 and U(e) = 1.

The utilities assigned to bundles in Figure 4.2 are ranked in the same way as the bundles themselves. In making choices, Pandora therefore behaves as though she were maximizing the value of U. But she also behaves as though she were maximizing the value of the alternative utility function V given in Figure 4.2. This observation signals the fact that there are many ways in which we could have assigned utilities to the bundles in a manner consistent with Pandora's preferences. The only criterion that is relevant when picking one of the infinity of utility functions that represent a given preference relation is that of mathematical convenience.

4.3.3 Rational Choice Theory?

Outside economics, the use of utility theory is controversial. In political science, the debate over "rational choice theory" often gets quite heated.

However, both sides in such debates commonly subscribe to the causal utility fallacy, which says that decision makers choose a over b because the utility of a exceeds that of b. But modern economists don't argue that a person's choice of a over b is caused by the utility of a exceeding that of b. On the contrary, it is because the preference a ≻ b has been revealed that we choose a utility function satisfying u(a) > u(b).

For people to behave as though their aim were to maximize a utility function, it is only necessary that their choice behavior be consistent. To challenge the theory, you therefore need to argue that people behave inconsistently, rather than that they don't really have utility generators inside their heads. As for the critics who claim that economists believe that people have little cash registers in their heads that respond only to dollars, they haven't bothered to study the theory they are criticizing at all.

## 4.4 Dicing with Death

The game of Russian Roulette will allow us to review some of the ideas that we met in Chapters 2 and 3 while focusing our attention on the inadequacy of what has been said so far about utility functions.

Boris and Vladimir are officers in the service of the czar who have both fallen in love with a beautiful Muscovite maiden called Olga. They agree that it doesn't make sense for both to press their claims simultaneously but disagree on who should back down. Eventually they decide to settle the matter with a game of Russian Roulette, with Boris as player I and Vladimir as player II.

In Russian Roulette, a bullet is loaded at random into one of the chambers of a six-shooter, as illustrated in Figure 4.3(a). The players then take turns pointing the revolver at their heads. When it is your turn, you can either pull the trigger or chicken out. Chickening out and death disqualify you from chasing after Olga any more. One might think that only crazy people would play such a game, but the superlatively creative French mathematician Evariste Galois died at the age of twenty while playing something very similar. Perhaps this is why economists prefer to assume that people are rational rather than crazy.

Perhaps this is why Russians call the game French Roulette.

Neither Boris nor Vladimir cares about the welfare of the other, so each player distinguishes only three outcomes, L, D, or W, which we can think of as death, disgrace, or triumph. Player i’s preferences over these outcomes satisfy L ⊲ D ⊲ W.

The outcome L corresponds to a player shooting himself. The outcome W corresponds to his being left to woo Olga undisturbed. The outcome D corresponds to a player chickening out. He will then be forced to sit alone, morosely drinking vodka in the officer’s club, while his rival trifles with Olga’s affections.

4.4.1 Version 1 of Russian Roulette A natural way of drawing the game tree for Russian roulette is shown in Figure 4.4. The act of loading the single bullet into the gun is represented by a single chance move that opens the game. Each of the six chambers of the revolver corresponds to one of the six choices available to Chance at this node. The chambers are labeled 1 through 6, according to the order in which they will be reached as the trigger is pulled. Each chamber is equally likely to be chosen, and so the probability that the bullet is in any particular chamber is 1/6.

(a) Russian Roulette (b) Zeckhauser’s Paradox Figure 4.3 Where are the bullets?

The branches at decision nodes are labeled A (for across) and D (for down). Playing down corresponds to chickening out. Playing across corresponds to a player pulling the trigger.

The nodes at which a player chooses between A or D are labeled with the number of the chamber that contains the bullet. The information sets in Figure 4.4 indicate the fact that the players don’t know this information when they decide whether or not to pull the trigger.

Since all but one of the information sets contain more than one decision node, this version of Russian Roulette is a game of imperfect information. A pure strategy in a game of imperfect information specifies an action only at each of a player’s information sets—not at each of his decision nodes.

The pure strategy pair (AAA, AAD) is indicated in Figure 4.4 by doubling appropriate branches. All six across branches have therefore been doubled at player I’s first information set. He can’t plan to play differently at different nodes in the same information set because he won’t be able to distinguish between them when he makes his decision.

Once Boris and Vladimir have chosen their pure strategies, the course of the game is entirely determined, except for the initial decision made by Chance. If Chance puts the bullet in chamber 6, the resulting play of the game starts at the root and proceeds vertically downward to the first node labeled with a 6, where it is Boris’ turn to move. His choice of pure strategy AAA requires that he take action A at his first move. Accordingly, he pulls the trigger but survives because the bullet isn’t in chamber 1. We therefore move on to the second node labeled with a 6, where it is Vladimir’s turn to move. His choice of pure strategy AAD requires that he take action A at his first move. So he pulls the trigger but survives because the bullet isn’t in chamber 2.

The play continues horizontally in this way until it reaches the node labeled with 6* at the bottom right of Figure 4.4, where it is Vladimir’s move.

Vladimir now knows that the bullet is in chamber 6, and so he is sure to shoot himself if he pulls the trigger. Fortunately, his choice of the pure strategy AAD requires that he chicken out by taking action D at his third move. This action concludes the play that started with Chance putting the bullet in chamber 6 by taking it downward to a payoff box in which Boris gets the outcome W and Vladimir gets the outcome D.

While following this play, we always knew where the bullet was, but the players were in suspense until node 6* was reached. For example, Vladimir didn’t know he was about to pull the trigger on an empty chamber at his second move. We knew the game had reached node 6, but Vladimir thought that nodes 4 and 5 in his second information set were just as likely. When he pulled the trigger, he therefore thought he would shoot himself with probability 1/3 since this is the conditional probability of being at node 4, given that Vladimir’s second information set has been reached.

4.4.2 Version 2 of Russian Roulette Figure 4.5 shows an alternative game tree for Russian Roulette. No information sets appear because the new version is a game of perfect information. The price paid for this simplification is that we have to include six chance moves: one for each chamber of the six-shooter.

On the other hand, the new game has lots of subgames that we will exploit when using backward induction to solve the game in Section 4.7. By contrast, version 1 of Russian roulette has only two subgames: the whole game and the one-player subgame rooted at node 6*. No decision node with companions in its information set can serve as the root of a subgame because we can’t disentangle such a node from its companions without making nonsense of the informational assumptions of the game.

The strategy pair (AAA, AAD) has been indicated by doubling branches in Figure 4.5. Its use results in the various leaves being reached with the probabilities written beneath them. Boris ends up with the outcome W half the time and with L the rest of the time. If the strategy pair (DDD, AAD) were used instead, Boris would get D for certain.

If Boris knows or guesses that Vladimir will choose AAD, which of AAA or DDD is better for him? It is important to recognize that we can’t answer this question without knowing more about Boris’s preferences.

All we have been told so far is that L ⊲ D ⊲ W, but this information doesn’t help us decide whether Boris prefers D for certain to the lottery in which he is equally likely to get W or L. If Boris were young and romantic like Evariste Galois, he might be willing to risk death rather than abandon his beloved, but disillusioned old gentlemen like me won’t see the potential reward as being worth much of a risk.

However, both of us will agree that D is an outcome intermediate between W and L.

## 4.5 Making Risky Choices

How do we describe a player’s preferences over lotteries that involve more than two prizes? A naive approach would be to replace all the prizes in the lotteries by their worth to the player in money. Wouldn’t a rational person then simply prefer whichever of two lotteries has the larger dollar expectation?

The story coming up next explains why such an approach won’t work. Like Russian Roulette, it is set in the last days of the czars.

4.5.1 The St. Petersburg Paradox Nicholas Bernouilli proposed the following paradox about a casino in St. Petersburg that was supposedly willing to run any lottery whatever, provided that the management could set the price of a ticket to participate.3 In the lottery of Figure 4.6, a fair coin is tossed until it shows heads for the first time. If the first head appears on the kth trial, you win $2k. How much should you be willing to pay in order to participate in this lottery?

Since each toss of the coin is independent, the probability of winning $2k is calculated as shown below for the case k=4: prob(TTTH) = prob(T) × prob(T) × prob(T) × prob(H) = (1/2)^4 = 1/16.

The expectation in dollars of the St. Petersburg lottery L is therefore E(L) = 2prob(H) + 4prob(TH) + 8prob(TTH) + … = 2 × (1/2) + 4 × (1/4) + 8 × (1/8) + … = 1 + 1 + 1 + 1 + …, which implies that its expected dollar value is “infinite.” Should Olga therefore be willing to sell off all she owns and borrow as much as she can in order to buy a lottery ticket? Since the probability is 7/8 that she will end up with no more than $8, she is unlikely to find the odds attractive.

The moral isn’t that the policy of always choosing the lottery with the largest expectation in dollars is necessarily irrational. The St. Petersburg story merely casts doubt on the claim that no other policy can be rational.

The same goes for any theory that claims that there is only one rational way to respond to risk. An adequate theory needs to recognize that the extent to which Olga is willing to bear risk is as much a part of her preference profile as her relative liking for the songs that Boris and Vladimir sing when they play their balalaikas late at night beneath her bedroom window.

4.5.2 Von Neumann and Morgenstern Utility Rationality doesn’t require that Olga try to maximize her expected dollar value when choosing between lotteries. However, Von Neumann and Morgenstern gave a list of consistency postulates about preferences in risky situations that imply that Olga will behave as though maximizing the expected value of something when acting rationally. We call this something the Von Neumann and Morgenstern utility of a lottery.

The first postulate repeats the rationality assumption of Chapter 3: Postulate 1 A rational player prefers whichever of two win-or-lose lotteries offers the larger probability of winning.

Postulate 1 is about win-or-lose lotteries, in which the only prizes are drawn from the set O = {L, W}. A utility function u: O → ℝ that represents the preference W ⊲ L must have a = u(L) < u(W) = b.

The set of lotteries with prizes drawn from the set O will be denoted by lott(O). The win-or-lose lottery p in which Olga wins with probability p therefore belongs to lott({W, L}). The expected utility of p is Eu(p) = pu(W) + (1−p)u(L) = a + p(b−a). (4.1)

Since b−a > 0, Eu(p) is largest when the probability p of winning is largest.

Equation (4.1) tells us that Eu is a utility function for Olga’s preferences over lott(O) when O = {W, L}. Postulate 1 therefore implies that Olga necessarily acts as though maximizing expected utility when making decisions involving only lotteries whose prizes are L or W.

prize | $2 | $4 | $8 | $16 | . . . | $2^k | . . .

--- | --- | --- | --- | --- | --- | --- | --- coin sequence | H | TH | TTH | TTTH | . . . | TT...TH | . . .

probability | 1/2 | 1/4 | 1/8 | 1/16 | . . . | 1/2^k | . . .

Figure 4.6 The St. Petersburg lottery.

Matters become more complicated when there are prizes intermediate between W and L. It then ceases to be true that Eu is a utility function for Olga’s preferences over lotteries whenever u is a utility function for her preferences over prizes. If u: O → R is to be a Von Neumann and Morgenstern utility function—so that Eu represents Olga’s preferences over lotteries—we need to select u very carefully from the large class of utility functions that represent Olga’s preferences over prizes.

Postulate 2 Each prize o between the best prize W and the worst prize L is equivalent to some lottery involving only W and L.

The postulate says that, for each prize o in O, there is a probability q for which o ∼ qW ⊕ (1-q)L. (4.2)

The second postulate makes it possible to construct a Von Neumann and Morgenstern utility function u: O → R. The function u is defined so that the value of u(o) is the probability q in (4.2). That is to say, q = u(o) is defined to make Olga indifferent between getting o for certain and getting the lottery that yields W with probability u(o) and L with probability 1 - u(o).

For example, we might begin an experiment to elicit Olga’s preferences over risky prospects by asking her whether she will pay $20 for a ticket for the lottery q of (4.2) in the case when the best possible prize is W = $100 and the worst possible prize is L = $0. If she stops saying no and starts saying yes when q passes through the value 0.4, then u(20) = 0.4.

As we increase the price $X of a ticket from $0 to $100, u(X) will increase from u(0) = 0 to u(100) = 1. As we will see, the shape of the graph of u will tell us everything we need to know about Olga’s attitude to taking risks.

To confirm that u: O → R is a Von Neumann and Morgenstern utility function, we need to verify that Eu: lott(O) → R is a utility function for Olga’s preferences over lotteries. Figure 4.7 illustrates the two steps in the argument that justifies this conclusion. Each step requires a further postulate.

Postulate 3 Rational players don’t care if a prize in a lottery is replaced by another prize that they regard as equivalent to the prize it replaces.

The prizes available in the arbitrary lottery L of Figure 4.7 are o₁, o₂, ..., oₙ. By Postulate 2, Olga regards each such prize oₖ as the equivalent of some win-or-lose lottery qₖ W ⊕ (1-qₖ)L. Postulate 3 is then used to justify replacing each prize oₖ by the corresponding lottery qₖ W ⊕ (1-qₖ)L. We then need a final assumption to reduce the resulting compound lottery to a simple lottery.

Figure 4.7 Von Neumann and Morgenstern’s argument.

Postulate 4 Rational players care only about the total probability with which they get each prize in a compound lottery.

The total probability of W in Figure 4.7 is r = p₁q₁ + p₂q₂ + ... + pₙqₙ. Postulate 4 then says that we can replace the compound lottery by the simple lottery r W ⊕ (1-r)L, thereby justifying the second of the two steps the figure illustrates.

By Postulate 1, Olga prefers whichever of two lotteries like L in Figure 4.7 has the larger value of r = p₁q₁ + p₂q₂ + ... + pₙqₙ. She therefore acts as though seeking to maximize r = p₁q₁ + p₂q₂ + ... + pₙqₙ = p₁u(o₁) + p₂u(o₂) + ... + pₙu(oₙ)

= Eu(L).

Thus Eu: lott(O) → R is a utility function that represents Olga’s preferences in lotteries. But this is what it means to say that u: O → R is a Von Neumann and Morgenstern utility function for her preferences over prizes.

4.5.3 Attitudes to Risk How does Von Neumann and Morgenstern’s theory deal with the St. Petersburg paradox? Suppose that Olga’s utility for money is given by the Von Neumann and Morgenstern utility function u: R₊ → R defined by u(x) = 4√x. (4.3)

Her expected utility for the St. Petersburg lottery L of Figure 4.6 is then Eu(L) = (1/2)u(2) + (1/2²)u(2²) + (1/2³)u(2³) + ...

= 4{ (1/2)√2 + (1/2²)√(2²) + (1/2³)√(2³) + ... } = 4√2 { 1/2 + (1/2²) + (1/2³) + ... } = 4√2 * 1/(2-1) ≈ 4 * 2.42.

Olga is indifferent between the lottery L and $X if and only if their utilities are the same. So $X is the dollar equivalent of the lottery L if and only if u(X) = Eu(L)

4√X ≈ 4 * 2.42 X ≈ (2.42)² ≈ 5.86.

Thus Olga won’t pay more than $5.86 to participate in the St. Petersburg lottery—which is a lot less than the infinite amount she would pay if her Von Neumann and Morgenstern utility function were u(x) = x. We will see that the reason we get such a different result is that Olga’s new Von Neumann and Morgenstern utility function makes her risk averse instead of risk neutral.

Paradox of the Infinite? Is the St. Petersburg paradox really resolved? If u(x) → ∞ as x → ∞, we can revive the paradox simply by choosing a different lottery L for which Eu(L) is infinite.

Mathematicians control such problems of the infinite by imposing extra postulates that ensure that a Von Neumann and Morgenstern utility function is bounded when the number of prizes is allowed to be infinite. For example, we could insist that rational players are never caught out by the Box Swapping paradox of Exercise 4.11.27.

However, nothing prevents our working with unbounded utility functions, provided we do only those things that are sanctioned by Von Neumann and Morgenstern’s postulates. In particular, we must stick to lotteries that lie between some worst outcome L and some best outcome W, although there is no harm in allowing lotteries with an infinite number of prizes when this constraint is observed. We can even allow L and W themselves to be such infinite lotteries since the Von Neumann and Morgenstern methodology will necessarily assign them both a finite expected utility. What this means in practice is that you don’t need to worry that a Von Neumann and Morgenstern utility function is unbounded if you only plan to consider lotteries whose expected utility is finite. This is why the standard resolution of the St. Petersburg paradox with u(x) = 4√x is legitimate.

It doesn’t help to try to make W and L the limits of infinite lotteries whose probabilities are progressively shifted outward toward dollar prizes that are increasingly positive or negative. The limiting value of the probability assigned to any particular prize would then be zero, but W and L can’t have zero probabilities assigned to all their prizes.

4.5.4 Risk Aversion The dollar expectation of the lottery M in Figure 4.8 is EM = 3/4 * 1 + 1/4 * 9 = 3.

If Olga’s Von Neumann and Morgenstern utility for $x continues to be u(x) = 4√x, as in equation (4.3), her expected utility for M is Eu(M) = 3/4 u(1) + 1/4 u(9) = 3/4 * 4√1 + 1/4 * 4√9 = 3 + 3 = 6.

It follows that u(EM) = u(3) = 4√3 ≈ 6.93 > 6 = Eu(M), and so Olga would rather not participate in the lottery if she can have its expected dollar value for certain instead.

If Olga would always sell a ticket for a lottery with money prizes for an amount equal to its expected dollar value, she is risk averse over money. If she would always buy a ticket for a lottery for an amount equal to its expected dollar value, then she is risk loving. If she is always indifferent between buying and selling, she is risk neutral. The graphs of utility functions that represent risk-averse, risk-neutral and risk-loving preferences are shown in Figure 4.9. As we saw in Figure 4.8, chords drawn to the graph of the utility function of a risk-averse person lie on or below the graph. Mathematicians say that such functions are concave. A function whose chords lie on or above its graph is convex. A person with a convex Von Neumann and Morgenstern utility function is risk loving.

A function with a straight-line graph is commonly said to be “linear,” but the proper mathematical term is affine. If Olga has an affine Von Neumann and Morgenstern utility function, she is always indifferent between buying or selling a lottery for an amount equal to its expected value in dollars and so is simultaneously risk loving and risk averse.

The fallacy that makes the St. Petersburg story seem paradoxical is that rational people are necessarily risk neutral. If Olga were risk neutral (or risk loving), she would be willing to pay an infinite amount to participate.
