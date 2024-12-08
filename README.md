PACSNAKE

Video Demo: https://youtu.be/HfswgS8xb04

Description:

This is the classic Snake game but with a Pac-Man twist that I came up with brainstorming for ideas. For this project I knew wanted to learn how to use Pygame, which I think I remember being talked about in class, but is definitely popular for some of the final projects ive seen on the cs50 website. Im not a programmer so this was all new to me and wasn’t even sure what Pygame was when I started, nor how the Vector2 worked. I generated several examples of snake games from chatgpt just to get an idea of how to even make such a game, and referenced some of the code from that to get a bare-bones working model.

From that I got the hang of the mechanics and how to move things around, edit the objects, duplicate them, etc. From there it was a great and fun experience making it into a pacman themed game with sounds, background, etc. If i got big errors I used the duck for help and to pare the code down which had a lot of repetition from adding the ghosts and sounds, etc. It was an interesting learning experience. Some of the weird errors i got were a looping intro song, I figured out that I needed to end each game and start without a collision which had been working just fine but the loop caused issues with the music in practice. Making the snake was a lot of work...how do you make a pacman snake? lol I had to play with the design since i wanted the head to be notable, finally decided to make each segment a circle to make the head stand out - that required using pics for each segment vs the typical fill in a square method.

For the actual program the first section is building the pacsnake. For this I used Vector2 to place the snake on the background, roughly where pacman would start, and provide the movement using the vectors. The movement basically just shifts the segments forward and makes a new head based on the movement. I built the snake from png pics I made on my macbook. the body is actually just a revered pacman head to make a solid yellow circle. I added sounds that I found in a free database, all .wav files that seemed to be python friendly. You can see the head graphics next, this part was needed i found because when the snake moved the mouth didnt, so I had to add a head position for each direction. Then finally just a reset for when the snake died it would go back to the center.

The ghosts were simple. Each ghost is a png that is random position (via the imported random library) when "eaten" by the snake in the main section. Then the main section is the mechanics that "eat" each ghost and reset the snake if it touches itself or goes outside the game area (check fail section). Scoring seemed difficult at first but one of the AI programs came up with using the snake length minus 3 segments (the original snake), and that is what is displayed on the screen. The controls are down in the main game and each key has been paired with a movement/vector. I also made it so the game would not start (false) till one of the keys was pushed. I did this because when i had the snake stopped it kept "crashing" and when i fixed it by having the snake start moving right away self.direction = Vector2(1,0) it was super annoying! So this was my fix and it worked great. Last I added the the intro music to pair with the game initial start and the background.

Very glad for AI help on this one. I think I could have figured out a basic snake, but AI helped a lot to make it much better. One important note for class would be that I never got pygame to work in the cs50 codespace. I had to download VS code and use that, I spend a good few hours figuring that out (to include asking AI a lot why it wasnt working) so that would be a helpful note I'll include in my video. It wasn’t intuitive either, it would give a driver error and send you on a wild goose hunt for one, but none ever worked. Anyway, this was a great project, I learned a lot and had fun mixing the two games.


<!--
**ajpratt15/AJPratt15** is a ✨ _special_ ✨ repository because its `README.md` (this file) appears on your GitHub profile.

Here are some ideas to get you started:

- 🔭 I’m currently working on ...
- 🌱 I’m currently learning ...
- 👯 I’m looking to collaborate on ...
- 🤔 I’m looking for help with ...
- 💬 Ask me about ...
- 📫 How to reach me: ...
- 😄 Pronouns: ...
- ⚡ Fun fact: ...
-->
