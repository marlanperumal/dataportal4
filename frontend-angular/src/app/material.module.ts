import { ModuleWithProviders, NgModule } from '@angular/core';

import { MatToolbarModule } from '@angular/material/toolbar';
import { MatButtonModule } from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';
import { MatGridListModule } from '@angular/material/grid-list';
import { MatTabsModule } from '@angular/material/tabs';
import { MatMenuModule } from '@angular/material/menu';
import { MatDividerModule } from '@angular/material/divider';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatCardModule } from '@angular/material/card';
import { MatInputModule } from '@angular/material/input';

const modules = [
  MatToolbarModule,
  MatButtonModule,
  MatIconModule,
  MatGridListModule,
  MatTabsModule,
  MatMenuModule,
  MatCardModule,
  MatDividerModule,
  MatFormFieldModule,
  MatInputModule,
]

@NgModule({
  imports: modules,
  exports: modules,
})

export class MaterialModule {}
