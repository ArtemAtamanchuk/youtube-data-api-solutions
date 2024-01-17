# Get All Published Videos
This solution allows you to get data about all **published** videos on a YouTube channel. Published videos means they have been uploaded to the channel and are open access. So don't be surprised if you find a difference between the number of videos on your channel (this information is available in the Channel details section on the channel page) and the number of videos you uploaded.

To do this, you need `DEVELOPER_KEY` to assign the API key received in [Google Developers Console](https://console.cloud.google.com/apis/credentials). Assign the `CHANNEL_ID` variable to the channel id from which you will receive video data.

To get the channel id you can go to the main page of the channel, e. g., [https://www.youtube.com/@GoogleDevelopers](https://www.youtube.com/@GoogleDevelopers). After that, open the source code of this page (normally, it is a `Ctrl` + `U` keys combination). There, open a search tool on the page (`Ctrl` + `F`) and paste `<link rel="canonical"`. After that, you find a single match, which is a `link` tag with the `href` attribute containing the YouTube channel link at the end of which is its id. In our case, we have `<link rel="canonical" href="https://www.youtube.com/channel/UC_x5XG1OV2P6uZZ5FSM9Ttw">`: the `UC_x5XG1OV2P6uZZ5FSM9Ttw` combination is the Google for Developers channel id.

Of course, you can do all of this through a variety of web applications, such as [https://ytubetool.com/tools/youtube-channel-id](https://ytubetool.com/tools/youtube-channel-id).

It is all: you don't need to do something. Run the script and you will get a csv file (its name is `The List Videos From "the channel's title".csv`) wich has titles, URLs, and publish dates of all the videos of the channel. These items will be listed in order from oldest to newest.

You may notice that the video information is retrieved by working with a playlist containing all published videos. And you can access this playlist. You just need to replace the second character of the id of this channel (it is the `C` character) with the `U` character, insert the obtained combination into the following HTTP request: `https://www.youtube.com/playlist?list=` and then click on it and you will get to this playlist. Try it.
