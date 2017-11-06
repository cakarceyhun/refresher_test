function startWorker(callback) {
	if(typeof(Worker) !== "undefined") {
		if(typeof(w) == "undefined") {
			hash = '0ca975c72d63'
			w = new Worker("refresher.worker.js");
			w.postMessage('hash=' + hash + '&filename=content.txt')
		}
	}

	w.onmessage = function(event) {
		if (event.data.indexOf('refresh') >= 0) {
			callback()
		}
		w.postMessage('hash=' + hash + '&filename=content.txt')

	};
}


