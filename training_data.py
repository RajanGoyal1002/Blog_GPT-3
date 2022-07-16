# Format of training prompt
defaultPrompt = """I am an intelligent blog writer:
Input: Write blog on Quantum Computing.

Output:
Quantum computing is an area of computing where information is processed using quantum-mechanical phenomena, such as superposition and entanglement. A quantum computer harnesses these phenomena to perform operations on data that would be impossible for a classical computer.

The basic principle behind quantum computing is that a quantum bit (qubit) can represent a zero and a one at the same time, and that quantum computers can exploit this fact to solve certain problems much faster than classical computers. For example, a quantum computer could easily factor a large number into its prime factors, something that is very difficult for a classical computer.

-

Input: Write article on digital writing pad.

Output:
A digital writing pad is a great way to take notes, write essays, and even create entire documents without ever having to put pen to paper. You can find digital writing pads in a variety of sizes, styles, and price ranges, so finding one that meets your needs shouldn’t be difficult.

One of the great things about digital writing pads is that they allow you to make mistakes without having to start over from scratch. 
-

Input: Write blog on home made facial pack.

Output:

A facial pack made at home can be a refreshing and relaxing way to take care of your skin. You can make a facial pack with ingredients that you may already have in your kitchen, such as oatmeal, honey, and milk. This pack can be used to help exfoliate your skin and to draw out impurities.

To make the pack, simply combine 1/2 cup of oatmeal with 1/4 cup of milk and 1 tablespoon of honey. Mix the ingredients together until they form a thick paste. Apply the paste to your face and allow it to sit for 15-20 minutes. Rinse the pack off with warm water and pat your face dry.

You should feel a difference in your skin after just one use. Your skin will be softer and smoother, and it will have a healthy glow. This facial pack can be used once or twice a week, depending on your skin type.

Input: Write blog on explaning 5G technology, its usage, advantage and disadvantage.

Output:
5G technology is the fifth generation of wireless technology. It is the successor to 4G and is designed to provide faster speeds and more reliable connections. 5G technology is still in its early stages, but it is already being used in some parts of the world. 5G technology is expected to provide speeds of up to 10 gigabits per second, which is 10 times faster than current 4G speeds. 5G technology will also have lower latency, which means that it will be able to provide more responsive connections. 5G technology is still in its early stages, but it is already being used in some parts of the world. 5G technology is expected to provide speeds of up to 10 gigabits per second, which is 10 times faster than current 4G speeds. 5G technology will also have lower latency, which means that it will be able to provide more responsive connections.

There are many potential uses for 5G technology. One of the most promising applications is in the area of virtual reality. 5G technology will be able to provide the high speeds and low latency necessary to create realistic virtual environments. 5G technology could also be used to connect self-driving cars and other connected devices.

5G technology comes with some potential risks. One of the biggest concerns is that 5G technology will use higher frequency waves, which could potentially be harmful to human health. There is also a concern that 5G technology will be used for mass surveillance, as the high speeds and low latency will make it possible to collect large amounts of data.
-

Input: Write an article explaining meditation, types of meditation and their advantages with some examples.

Output:

Meditation is a practice where an individual uses a technique – such as mindfulness, or focusing their mind on a particular object, thought or activity – to train attention and awareness, and achieve a mentally clear and emotionally calm and stable state.

There are many different types of meditation, each with its own advantages. Some common types of meditation include:

1. Mindfulness meditation: This type of meditation involves focusing your attention on the present moment, and being aware of your thoughts, feelings and sensations without judgement. This can help to improve your focus and concentration, and reduce stress and anxiety.

2. Breath awareness meditation: This type of meditation involves focusing your attention on your breath, and being aware of the sensations of your breath as it enters and leaves your body. This can help to improve your respiratory function and reduce stress and anxiety.

-

Input: Write a blog on yoga 

Output:
Yoga is an ancient physical and mental discipline that originated in India. The word yoga comes from the Sanskrit word yuj, which means to yoke, or to unite. The practice of yoga is thought to help unite the mind, body, and spirit.

Yoga is a system of physical and mental exercises that includes breath control, simple meditation, and the adoption of specific bodily postures. Yoga is widely practiced for health and relaxation purposes.

The health benefits of yoga include:

1. Yoga can help to relieve stress and promote relaxation.

2. Yoga can help to improve flexibility and strength.

3. Yoga can help to improve your breathing.

4. Yoga can help to improve your circulation.


-


Input: Article on "How to deal with depression"

Output:
If you're feeling depressed, it's important to seek help from a professional. Depression is a serious condition that can have a negative impact on every aspect of your life. But with treatment, you can feel better and get back to enjoying your life.

There are a number of different types of treatment for depression. The most common is antidepressant medication. Antidepressants can help to improve your mood and give you more energy. They can also help to reduce anxiety and improve sleep.

Depression is a serious condition, but it is treatable. If you're feeling depressed, reach out for help. With treatment, you can feel better and get back to enjoying your life.
-


Input: {}

Output: """
