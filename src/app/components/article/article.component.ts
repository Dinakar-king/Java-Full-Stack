import { Component } from '@angular/core';
import { ArticleFormComponent } from "../article-form/article-form.component";
import { ArticleListComponent } from "../article-list/article-list.component";

@Component({
  selector: 'app-article',
  imports: [ArticleFormComponent, ArticleListComponent],
  templateUrl: './article.component.html',
  styleUrl: './article.component.css'
})
export class ArticleComponent {

}
