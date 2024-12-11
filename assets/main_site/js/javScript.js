



let isColorOne = true; // متغیر برای تعیین رنگ فعلی

setInterval(() => {
    const bgElement = document.querySelector('.bg-re'); // انتخاب عنصر با کلاس bg_re
    if (isColorOne) {
        bgElement.style.backgroundColor = '#d0e3b1'; // تغییر به رنگ دوم
    } else {
        bgElement.style.backgroundColor = '#ffb69f'; // تغییر به رنگ اول
    }
    isColorOne = !isColorOne; // تغییر وضعیت رنگ
}, 2500); // هر 30 ثانیه


let currentIndex = 0;
const images = [
    '../img/p1.png',
    '../img/r.png',
    '../img/p1.png',
    '../img/r.png' // لیست تصاویر
];

function changeImage(direction) {
    currentIndex += direction;

    // اگر به آخر لیست برسیم، به اول برمی‌گردیم
    if (currentIndex < 0) {
        currentIndex = images.length - 1;
    } else if (currentIndex >= images.length) {
        currentIndex = 0;
    }

    document.getElementById('galleryImage').src = images[currentIndex];
}


const search = document.querySelector('.search1')
const btn = document.querySelector('.btn1')
const input = document.querySelector('.input')

btn.addEventListener('click', () => {
    search.classList.toggle('active')
    input.focus()
})

function togglePassword() {
    var passwordField = document.getElementById("password");
    var passwordFieldType = passwordField.getAttribute("type");
    if (passwordFieldType === "password") {
        passwordField.setAttribute("type", "text");
    } else {
        passwordField.setAttribute("type", "password");
    }
}


                // Toggle the icon between » and « based on the state of the collapse
                    document.getElementById('toggleIcon').addEventListener('click', function () {
                        var icon = this;
                        var filterSections = document.querySelectorAll('.filter-collapse');
                        
                        filterSections.forEach(function(section) {
                            if (section.classList.contains('show')) {
                                icon.textContent = '«';
                            } else {
                                icon.textContent = '»';
                            }
                        });
                    });
                
                    // Automatically change icon on collapse events
                    document.querySelectorAll('.filter-collapse').forEach(collapseEl => {
                        collapseEl.addEventListener('shown.bs.collapse', function () {
                            document.getElementById('toggleIcon').textContent = '«';
                        });
                
                        collapseEl.addEventListener('hidden.bs.collapse', function () {
                            document.getElementById('toggleIcon').textContent = '»';
                        });
                    });
                
                    

    function selectColor(element) {
        // Remove 'color-selected' class from all colors
        document.querySelectorAll('.color').forEach(color => color.classList.remove('color-selected'));
        // Add 'color-selected' class to the selected color
        element.classList.add('color-selected');
    }




    const triggerTabList = document.querySelectorAll('#myTab button')
triggerTabList.forEach(triggerEl => {
  const tabTrigger = new bootstrap.Tab(triggerEl)

  triggerEl.addEventListener('click', event => {
    event.preventDefault()
    tabTrigger.show()

  })
})



// login
const inputField = document.getElementsByClassName('.input-field')
const placeholder = document.querySelector('.placeholder');

inputField.addEventListener('focus', () => {
    placeholder.classList.add('active');
});

inputField.addEventListener('blur', () => {
    if (!inputField.value) {
        placeholder.classList.remove('active');
    }
});




// shop filter

const filterToggle = document.getElementById("filterToggle");
const filterMenu = document.getElementById("filterMenu");
const toggleIcon = document.getElementById("toggleIcon");
const content = document.getElementById("content");
const par = document.querySelector(".par");
const par1 = document.querySelector(".par1");

filterToggle.addEventListener("click", () => {
  filterMenu.classList.toggle("hidden");
  content.classList.toggle("with-filter");

  // تغییر آیکون
  if (filterMenu.classList.contains("hidden")) {
    toggleIcon.textContent = ">";
    par.style.display = "flex"; 
    par1.style.display = "flex"; 
  } else {
    toggleIcon.textContent = "<";
    par.style.display = "none";
    par1.style.display = "none";
  }
});
