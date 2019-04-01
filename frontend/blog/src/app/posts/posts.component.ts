import { Component, OnInit, OnDestroy } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-posts',
  templateUrl: './posts.component.html',
  styleUrls: ['./posts.component.scss']
})
export class PostsComponent implements OnInit, OnDestroy {
  data: any
  private req: any
  url: string = '/getData/'

  constructor(private http:HttpClient) { }

  ngOnInit() {
  	this.req = this.http.get(this.url).subscribe(data => {
      this.data = data as [any]
    })
  }

  ngOnDestroy(){
    this.req.unsubscribe()
  }
}
