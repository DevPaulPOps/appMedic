package main

import (
	"log"
	"net/http"
	"fmt"
)

const PORT string = ":443"
const DIR = "./app-medic/browser/index.html"

func StartServer() error {
	fmt.Println("Starting server on port", PORT)
	fmt.Println("URL to access the server", "https://localhost" + PORT)
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		http.ServeFile(w, r, DIR)
	})

	err := http.ListenAndServe(PORT, nil)

}
func main() {

	err := StartServer()

	/**
	  Handle server errors so that the application doesn't crash,
	    and continues to run no matter what.
	*/
	if err != nil {
		switch err {
		case http.ErrServerClosed:
			log.Println("Server closed", err.Error())
		case http.ErrMissingFile:
			log.Println("File not found", err.Error())
		case http.ErrAbortHandler:
			log.Println("Handler aborted", err.Error())
		case http.ErrBodyNotAllowed:
			log.Println("Body not allowed", err.Error())
		case http.ErrHijacked:
			log.Println("Connection hijacked", err.Error())
		case http.ErrContentLength:
			log.Println("Content length error", err.Error())
		case http.ErrHandlerTimeout:
			log.Println("Handler timeout", err.Error())
		case http.ErrLineTooLong:
			log.Println("Line too long", err.Error())
		case http.ErrNotMultipart:
			log.Println("Not multipart", err.Error())
		case http.ErrMissingBoundary:
			log.Println("Missing boundary", err.Error())
		case http.ErrNoCookie:
			log.Println("No cookie", err.Error())
		case http.ErrUseLastResponse:
			log.Println("Use last response", err.Error())
		case http.ErrNoLocation:
			log.Println("No location", err.Error())
		case http.ErrSkipAltProtocol:
			log.Println("Skip alt protocol", err.Error())
		case http.ErrNotSupported:
			log.Println("Not supported", err.Error())
		default:
			log.Println("Error starting server", err.Error())
		}
	}
}
