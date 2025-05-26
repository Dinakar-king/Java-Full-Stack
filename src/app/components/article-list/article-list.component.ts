import { Component, OnInit } from '@angular/core';
import { ArticleService } from '../../services/article.service';
import { Article } from '../../models/article.model';
import { User } from '../../models/user.model';

@Component({
  selector: 'app-article-list',
  templateUrl: './article-list.component.html'
})
export class ArticleListComponent implements OnInit {
  articles: Article[] = [];
  displayedColumns: string[] = ['title', 'author', 'content', 'date'];

  // Mocked author list – match ids to names
  users: User[] = [
    { id: 1, username: 'John Doe', email: 'john@example.com' },
    { id: 2, username: 'Jane Smith', email: 'jane@example.com' }
  ];

  constructor(private articleService: ArticleService) {}

  ngOnInit(): void {
    this.articleService.getArticles().subscribe((data) => {
      this.articles = data;
    });
  }

  getAuthorName(id: number | null): string {
    const user = this.users.find(u => u.id === id);
    return user ? user.username : 'Unknown';
  }
}
