import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { ArticleService } from '../../services/article.service';
import { Article } from '../../models/article.model';
import { User } from '../../models/user.model';
import { Category } from '../../models/category.model';

@Component({
  selector: 'app-article-form',
  templateUrl: './article-form.component.html',
  styleUrls: ['./article-form.component.css'],
  standalone: true,
  imports: [
    // Angular core and material modules...
  ]
})
export class ArticleFormComponent implements OnInit {
  article: Article = {
    title: '',
    content: '',
    author_id: null,
    categories: []
  };

  users: User[] = [];
  categories: Category[] = [];

  constructor(
    private articleService: ArticleService,
    private route: ActivatedRoute,
    private router: Router
  ) {}

  ngOnInit(): void {
    this.loadUsers();
    this.loadCategories();

    const articleId = this.route.snapshot.paramMap.get('id');
    if (articleId) {
      this.articleService.getArticleById(articleId).subscribe(
        (data) => (this.article = data),
        (err) => this.router.navigate(['/articles'])
      );
    }
  }

  private loadUsers(): void {
    this.users = [
      { id: 1, username: 'John Doe', email: 'john@example.com' },
      { id: 2, username: 'Jane Smith', email: 'jane@example.com' }
    ];
  }

  private loadCategories(): void {
    this.categories = [
      { id: 101, name: 'Tech' },
      { id: 102, name: 'Science' },
      { id: 103, name: 'News' }
    ];
  }

  submitForm(): void {
    if (this.article.id) {
      this.articleService.updateArticle(this.article.id, this.article).subscribe(() => {
        this.router.navigate(['/articles']);
      });
    } else {
      this.articleService.addArticle(this.article).subscribe(() => {
        this.router.navigate(['/articles']);
      });
    }
  }

  cancel(): void {
    this.router.navigate(['/articles']);
  }
}
