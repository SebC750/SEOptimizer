# SEOptimizer
A proprietary offline desktop app to convert files such as images and videos to other file types. This application is being made for the purpose of providing for myself a tool to process files and convert them into lighter file types for SEO while securely handling client's assets.

## Motivation
As a full stack developer that primarily works with web applications, one of the most important concerns I often take into account is SEO (Search Engine Optimization). One of the ways I improve SEO is to convert files into more lightweight file types. For example, I will need to convert jpgs and pngs to webp type files as webps are often smaller in file size.

Of course, there are websites online that provide services for file conversions. However, my concern is that these websites have their own backend servers where they store images and videos for some time. They also are or at least have a free tier, which means they may perhaps look to other means of profiting that may be nefarious. As a professional app developer who works with clients, I usually have to handle assets provided by them that include sensitive information such as profile pictures or personal videos or even original works etc. This places great responsibility on me to ensure that such data is not carelessly uploaded to dubious sites for the sake of convenience.

This is why I decided to create my own offline desktop app that allows me to perform file conversions and keep track of assets without needing an internet connection. This allows me to keep all of my client's assets stored locally within my machine and only in that machine, ensuring security for my clients. Secure storage and processing of their files is a top priority.

## Features
The desktop app includes several features including:

- Electron.js: A cross-platform desktop framework for creating desktop apps using web technologies (HTML, CSS, JS/TS, React, TailwindCSS)

- FFMpeg: A file conversion program which enables us to perform edits and conversion of various files types.

- SQLite3: An embedded SQL database meant to store metadata of the files processed in the system. This allows me to keep track of files processed and to which project or client it belongs to as well as its location in the file system.

## Tech stack
- JavaScript
- TailwindCSS
- Node.js
- SQLite3
