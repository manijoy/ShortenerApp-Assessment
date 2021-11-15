import { HttpClient } from '@angular/common/http';
import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'twitter';
  shortURL = '';
  longURL = '';
  allURLs: any = []
  maxId: any = 0;
  hitCount: any = 0;
  redirectId = 0
  constructor(private http: HttpClient) {
  }

  ngOnInit() {
    if (window.location.pathname == '/') {
      this.getAllRequests();
    } else {
      this.getURL().subscribe(
        (data: any) => {
          console.log(data);
          if (data.length > 0 ) {
            this.hitCount = data[0].hitcount
            this.redirectId = data[0].id
            this.increaseHitCount()
            window.location.replace(data[0].longurl);
          }
        },
        (error: any) => {
  
        }
      )
    }
  }

  increaseHitCount() {
    this.putURL().subscribe(
      (data: any) => {
        console.log(data);
      },
      (error: any) => {

      }
    )
  }

  getAllRequests() {
    this.getAll().subscribe(
      (data: any) => {
        console.log(data);
        this.allURLs = data;
        this.allURLs.forEach((element: any) => {
          if (element.id > this.maxId) {
            this.maxId = element.id;
          }
        });
      },
      (error: any) => {

      }
    )
  }

  getShortenURL() {
    this.postURL().subscribe(
      (data: any) => {
        console.log(data);
        this.shortURL = data.shorturl;
        this.getAllRequests();
      },
      (error: any) => {

      }
    )
  }

  getAll() {
    return this.http.get('http://127.0.0.1:5000/urls');
  }

  postURL() {
    let data = {
      "hitcount": 0,
      "longurl": this.longURL,
      "shorturl": "http://localhost:4200/" + (this.maxId + 1)
    }
    return this.http.post('http://127.0.0.1:5000/urls', data);
  }

  getURL() {
    let data = {
      "shorturl": window.location.href
    }
    return this.http.post('http://127.0.0.1:5000/url/1', data);
  }

  putURL() {
    let data = {
      "hitcount": this.hitCount + 1
    }
    return this.http.put('http://127.0.0.1:5000/url/' + this.redirectId, data);
  }
}
