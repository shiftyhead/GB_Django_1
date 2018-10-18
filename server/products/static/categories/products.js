const Image = href => (
  `<div class="item__image" style="background-image: url(${ href })"></div>`
)

const Product = ({ id, name, image, cost }) => (
  `<div class="item">
      <a href="products/${ id }">
          ${ Image(`${ image }`) }
          <h2>${ name }</h2>
          <h3>${ cost }</h3>
      </a>
  </div>`
)

const renderData = res => {

  prod_html = res.data.results.map(Product)
    .join('')

  container = document.getElementById('product__list')

  container.innerHTML = container.innerHTML + prod_html
}
