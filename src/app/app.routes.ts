// src/app/app.routes.ts
import { Routes } from '@angular/router';
import { ArticleListComponent } from './components/article-list/article-list.component';
import { ArticleFormComponent } from './components/article-form/article-form.component';
// ... other component imports you might have

export const routes: Routes = [
  { path: '', redirectTo: '/articles', pathMatch: 'full' }, // Default route
  { path: 'articles', component: ArticleListComponent },
  { path: 'articles/new', component: ArticleFormComponent }, // <-- CHANGED 'add' to 'new' here
  { path: 'articles/edit/:id', component: ArticleFormComponent },
  // Add a fallback route if you like, e.g., for 404
  // { path: '**', redirectTo: '/articles' }
];