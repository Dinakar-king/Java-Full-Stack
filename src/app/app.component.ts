// src/app/app.component.ts
import { Component } from '@angular/core';
import { RouterOutlet, RouterLink } from '@angular/router';
import { CommonModule } from '@angular/common';

// Angular Material Imports
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatButtonModule } from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';

// IMPORTANT: Make sure this import path is correct for your HeaderComponent
// Assuming header.component.ts is directly under src/app/header/
import { HeaderComponent } from './header/header.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [
    HeaderComponent,
    ArticleListComponent,
    ArticleFormComponent,
    RouterModule // for <router-outlet>
  ],
  templateUrl: './app.component.html',
})
export class AppComponent {}
