// Adapted from: https://www.geeksforgeeks.org/how-to-draw-with-mouse-in-html-5-canvas/

const http = new XMLHttpRequest(); 

window.addEventListener('load', ()=>{ 
	resize(); // Resizes the canvas once the window loads 
	document.addEventListener('mousedown', startPainting); 
	document.addEventListener('mouseup', stopPainting); 
	document.addEventListener('mousemove', sketch); 
	window.addEventListener('resize', resize); 
}); 
	
const canvas = document.querySelector('#canvas'); 

// Context for the canvas for 2 dimensional operations 
const ctx = canvas.getContext('2d'); 
	
// Resizes the canvas
function resize(){ 
	ctx.canvas.width = 200
	ctx.canvas.height = 200 
} 
	
// Stores the initial position of the cursor 
let coord = {x:0 , y:0}; 

// This is the flag that we are going to use to 
// trigger drawing 
let paint = false; 
	
// Updates the coordianates of the cursor when 
// an event e is triggered to the coordinates where 
// the said event is triggered. 
function getPosition(event){ 
	coord.x = event.clientX - canvas.offsetLeft - 20; 
	coord.y = event.clientY - canvas.offsetTop - 20; 
} 

// The following functions toggle the flag to start 
// and stop drawing 
function startPainting(event){ 
	paint = true; 
	getPosition(event); 
} 

function stopPainting(){ 
	paint = false; 
} 
	
function sketch(event){ 
	if (!paint) return; 
	ctx.beginPath(); 
		
	ctx.lineWidth = 8; 

	// Sets the end of the lines drawn 
	// to a round shape. 
	ctx.lineCap = 'round'; 
		
	ctx.strokeStyle = 'black'; 
		
	// The cursor to start drawing 
	// moves to this coordinate 
	ctx.moveTo(coord.x, coord.y); 

	// The position of the cursor 
	// gets updated as we move the 
	// mouse around. 
	getPosition(event); 

	// A line is traced from start 
	// coordinate to this coordinate 
	ctx.lineTo(coord.x , coord.y); 
		
	// Draws the line. 
	ctx.stroke(); 
}

function predict(){

	let outputShow = document.querySelector("#show"); 

	image = canvas.toDataURL('image/png')

	http.open('POST', '/predict')
	http.send(image)

	ctx.clearRect(0, 0, canvas.width, canvas.height);

	 http.onload = function() {
	 	if (http.status === 200) {
	 		outputShow.textContent = http.response;
	 	}
	 	else {
	 		console.log('Something went wrong')
	 	}
	 }
}
