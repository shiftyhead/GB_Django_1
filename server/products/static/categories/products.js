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

const Next = href => (
  `<div class="next">
      <a href="${ href }">
      </a>
  </div>`
)

const renderData = res => {
  next_html = res.data.next.Next
  prod_html = res.data.results.map(Product)
    .join('')

  container = document.getElementById('product__list')

  container.innerHTML = container.innerHTML + prod_html +
  `<div class="prev"><a href="${ res.data.previous }">Previous</a></div>` +
  `<div class="next"><a href="${ res.data.next }">Next</a></div>`

}
