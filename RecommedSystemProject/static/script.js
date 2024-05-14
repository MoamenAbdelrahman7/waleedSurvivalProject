// // Define request options
// const requestOptions = {
//     method: 'POST', // Specify the HTTP method here (e.g., 'GET', 'POST', 'PUT', 'DELETE')
//     headers: {
//       'Content-Type': 'application/json' // Set the content type if sending data
//       // You can add other headers if needed
//     },
//     // You can include a body if it's a POST or PUT request
//     // body: JSON.stringify({ key: 'value' }) 
//   };
  
//   // Make a POST request with the specified options
//   fetch('/api/data', requestOptions)
//     .then(response => {
//       // Check if the response is successful
//       if (!response.ok) {
//         throw new Error('Network response was not ok');
//       }
//       // Parse the JSON response
//       return response.json();
//     })
//     .then(data => {
//       // Handle successful response
//       console.log(data);
//       // Update UI or do something with the data
//     })
//     .catch(error => {
//       // Handle error
//       console.error('Error fetching data:', error);
//     });
  



    // const all_videos = [
    //     "video1.mp4",
    //     "video2.mp4",
    //     "video3.mp4",
    //     "video4.mp4",
    //     "video5.mp4",
    //     "video6.mp4",
    //     "video7.mp4",
    //     "video8.mp4",
    //     "video9.mp4",
    //   ];
    //
    //   // Reference to the container element where videos will be appended
    //   const videosContainer = document.querySelector('.app__videos');
    //
    //   // Iterate over the list of videos
    //   all_videos.forEach((videoUrl, index) => {
    //     // Create video element
    //     const videoElement = document.createElement('div');
    //     videoElement.classList.add('video');
    //
    //     // Set video source
    //     const videoPlayer = document.createElement('video');
    //     videoPlayer.classList.add('video__player');
    //     videoPlayer.setAttribute('src', videoUrl);
    //     videoPlayer.setAttribute('loop', '');
    //     // videoPlayer.setAttribute('autoplay', '');
    //     videoElement.appendChild(videoPlayer);
    //
    //     // Create sidebar
    //     const sidebar = document.createElement('div');
    //     sidebar.classList.add('videoSidebar');
    //
    //     // Sidebar buttons
    //     const buttons = ['favorite_border', 'message', 'share'];
    //     buttons.forEach(icon => {
    //       const button = document.createElement('div');
    //       button.classList.add('videoSidebar__button');
    //       const iconSpan = document.createElement('span');
    //       iconSpan.classList.add('material-icons');
    //       iconSpan.textContent = icon;
    //       button.appendChild(iconSpan);
    //       const count = document.createElement('p');
    //       count.textContent = '0'; // You can set the actual count here
    //       button.appendChild(count);
    //       sidebar.appendChild(button);
    //     });
    //     videoElement.appendChild(sidebar);
    //
    //     // Create footer
    //     const footer = document.createElement('div');
    //     footer.classList.add('videoFooter');
    //
    //     // Footer text
    //     const text = document.createElement('div');
    //     text.classList.add('videoFooter__text');
    //     const title = document.createElement('h3');
    //     title.textContent = 'Video Title'; // You can set the actual title here
    //     text.appendChild(title);
    //     const description = document.createElement('p');
    //     description.classList.add('videoFooter__description');
    //     description.textContent = 'Video Description'; // You can set the actual description here
    //     text.appendChild(description);
    //     footer.appendChild(text);
    //
    //     // Footer ticker
    //     const ticker = document.createElement('div');
    //     ticker.classList.add('videoFooter__ticker');
    //     const tickerIcon = document.createElement('span');
    //     tickerIcon.classList.add('material-icons', 'videoFooter__icon');
    //     tickerIcon.textContent = 'music_note';
    //     ticker.appendChild(tickerIcon);
    //     const marquee = document.createElement('marquee');
    //     marquee.textContent = 'Song name'; // You can set the actual song name here
    //     ticker.appendChild(marquee);
    //     footer.appendChild(ticker);
    //
    //     // Footer record image
    //     const recordImage = document.createElement('img');
    //     recordImage.setAttribute('src', 'https://static.thenounproject.com/png/934821-200.png');
    //     recordImage.setAttribute('alt', '');
    //     recordImage.classList.add('videoFooter__record');
    //     footer.appendChild(recordImage);
    //
    //     videoElement.appendChild(footer);
    //
    //     // Append video element to container
    //     videosContainer.appendChild(videoElement);
    //   });
    //

    // icons script

    //  love icon script
    const love_icon=document.getElementById(`love_count_vid${ video.id }$`);
    const love_count=document.getElementById(`love_count_vid${ video.id }$`);
    love_icon.addEventListener("click",function(){
      if (love_icon.style.color != "red"){
        love_icon.style.color="red";
      console.log(love_count.innerText);
      let old_love_count=parseInt(love_count.innerText);
      love_count.innerHTML=old_love_count+1;
      }
      
    });







