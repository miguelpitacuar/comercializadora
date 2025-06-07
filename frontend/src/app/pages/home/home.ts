import { Component } from '@angular/core';
import { Products } from '../../services/products';

@Component({
  selector: 'app-home',
  imports: [],
  templateUrl: './home.html',
  styleUrl: './home.scss',
})
export class Home {
  products: any[] = [];
  constructor(private productsService: Products) { }

  async ngOnInit() {
    this.products = await this.productsService.getProducts();
  }
}
