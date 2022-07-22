function modalEventHandler() {
    // elements
    const modal = document.querySelector("#modal");
    const popupList = document.querySelectorAll(".popup");
    const popupBtn = document.querySelector("#trading_btn");
    const popupInnerButtons = document.querySelectorAll("#modal button");

    // modal 띄우는 이벤트 등록
    popupBtn.addEventListener("click",function() {
        // modal.style.display = "block";
        modal.classList.add("activated");
        popupList[parseInt(Math.random() * 3)].classList.add("activated");
    })

    // modal 없애는 이벤트 등록
    for (const btn of popupInnerButtons) {
        btn.addEventListener("click", function() {
            modal.classList.remove("activated")
            for (const e of popupList) {
                e.classList.remove("activated")
            }
        })
    }

}

modalEventHandler();