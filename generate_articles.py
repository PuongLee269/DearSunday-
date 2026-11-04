from pathlib import Path
from html import escape
import json
import re

ROOT = Path(__file__).parent
(ROOT / "blog").mkdir(exist_ok=True)
PAGE = "https://www.facebook.com/profile.php?id=61594563777409"
SITE = "https://puonglee269.github.io/DearSunday-/"
ARTICLES = [
    {
        "slug": "homestay-rieng-tu-cho-cap-doi-thanh-xuan",
        "n": "01",
        "tag": "HOMESTAY RIÊNG TƯ · THANH XUÂN",
        "title": "Homestay Thanh Xuân cho 1–2 người: DearSunday",
        "title_suffix": "Cẩm nang",
        "desc": "Tìm homestay Thanh Xuân cho 1–2 người? Tìm hiểu DearSunday ở Triều Khúc và các thông tin nên xác nhận về lịch, chi phí, không gian trước khi đặt.",
        "modified": "2026-11-04",
        "image": "room-bed-art.webp",
        "alt": "Giường với gối hình vịt màu vàng và những bức tranh vẽ nhiều màu trên tường",
        "faq_q": "DearSunday ở khu vực nào?",
        "faq_a": "DearSunday ở khu vực Triều Khúc, Thanh Xuân, Hà Nội. Địa chỉ cụ thể được gửi riêng sau khi đặt.",
        "faq_extra": [("DearSunday dành cho mấy người?", "DearSunday dành cho 1–2 người. Hãy nhắn Page để xác nhận thông tin phù hợp với ngày và kế hoạch của bạn."), ("Lịch và chi phí có cố định không?", "Lịch trống và chi phí cần được xác nhận theo ngày, khung giờ và lựa chọn dịch vụ. Nhắn Page DearSunday để nhận thông tin hiện tại trước khi đặt."), ("Giá homestay Thanh Xuân của DearSunday được tính thế nào?", "Chi phí cần được xác nhận theo ngày, khung giờ và dịch vụ bạn chọn; bài này không niêm yết mức giá cố định. Khi hỏi, hãy xin tổng chi phí và các khoản đã bao gồm trước khi đặt.")],
        "toc": [("Bắt đầu từ khu vực", "khu-vuc"), ("Chọn không gian hợp kế hoạch", "khong-gian"), ("Đối chiếu sức chứa và mục đích", "muc-dich"), ("Kiểm tra thông tin trước khi đi", "kiem-tra"), ("Các điểm cần xác nhận", "diem-can-xac-nhan")],
        "body": """<p class="lead"><strong>DearSunday là homestay dành cho 1–2 người ở khu vực Triều Khúc, Thanh Xuân, Hà Nội.</strong> Nếu đang tìm homestay Thanh Xuân, hãy đối chiếu khu vực, sức chứa, khung giờ và điều kiện đặt với kế hoạch của hai bạn. Lịch, chi phí và lựa chọn dịch vụ cần xác nhận trực tiếp trước khi chốt.</p>
<h2 id="khu-vuc">1. Bắt đầu từ khu vực</h2><p>Chọn khu vực thuận tiện cho điểm xuất phát và lịch trình của hai bạn. DearSunday ở khu vực Triều Khúc, Thanh Xuân, Hà Nội; địa chỉ cụ thể được gửi riêng sau khi đặt. Hãy hỏi hướng dẫn di chuyển trong tin nhắn riêng trước khi lên đường, không chia sẻ địa chỉ riêng tư ở nơi công khai.</p>
<h2 id="khong-gian">2. Chọn không gian hợp kế hoạch</h2><p>Đừng chỉ dựa vào ảnh trang trí. Nghĩ về cách hai bạn muốn dùng thời gian: nghỉ ngơi, trò chuyện hay cùng làm một hoạt động. Sau đó xem ảnh và mô tả hiện có để tự đánh giá liệu không gian có phù hợp với mục đích đó không. Nếu có điều kiện cụ thể quan trọng, hỏi trực tiếp thay vì suy luận từ ảnh.</p>
<h2 id="muc-dich">3. Đối chiếu sức chứa và mục đích</h2><p>Xác nhận số khách được nhận và liệu khung giờ phù hợp với kế hoạch. DearSunday dành cho 1–2 người. Nếu muốn thêm hoạt động như vẽ, nặn đất sét hoặc nấu ăn, Page giới thiệu các lựa chọn này; hãy hỏi hoạt động nào có vào ngày dự định cùng thời lượng và chi phí áp dụng.</p>
<h2 id="kiem-tra">4. Kiểm tra thông tin trước khi đi</h2><p>DearSunday giới thiệu khung ban ngày 12:30–20:30 (8 tiếng) và khung qua đêm 14:00–11:00 hôm sau. Lịch có thể thay đổi, nên xác nhận khung còn trống trước khi chốt. Hỏi rõ tổng chi phí, những gì đã bao gồm, quy định và cách nhận hướng dẫn đến nơi.</p>
<h2 id="diem-can-xac-nhan">5. Những điểm nên xác nhận trước khi đặt</h2><p>Dù chọn homestay nào ở Thanh Xuân, một tin nhắn hỏi rõ từ đầu sẽ giúp bạn tránh phải tự đoán thông tin. Có thể kiểm tra lần lượt:</p><ul class="quick-list"><li>Khu vực lưu trú và cách nhận hướng dẫn đến nơi</li><li>Sức chứa phù hợp với số người đi</li><li>Giờ bắt đầu, giờ kết thúc và lịch còn trống đúng ngày</li><li>Tổng chi phí, khoản đã bao gồm và phụ phí nếu có</li><li>Quy định lưu trú và tiện ích hoặc hoạt động bạn thật sự cần</li></ul><p>Với DearSunday, bạn có thể nhắn Page từ khóa <strong>“Sun”</strong>, kèm ngày dự định, số người và khung giờ muốn hỏi. Page sẽ xác nhận lịch và thông tin hiện tại; địa chỉ chi tiết được gửi riêng sau khi đặt.</p>""",
    },
    {
        "slug": "homestay-thue-theo-gio-ha-noi", "n": "02", "tag": "THUÊ HOMESTAY THEO GIỜ · HÀ NỘI",
        "title": "Thuê homestay theo giờ ở Hà Nội: cách chọn khung phù hợp",
        "desc": "Cách chọn thời lượng thuê homestay ở Hà Nội theo mục đích chuyến đi, thời gian di chuyển, giờ nhận-trả và chi phí cần xác nhận.",
        "image": "room-living-room.webp", "alt": "Không gian phòng khách sáng tại DearSunday, private homestay ở Hà Nội",
        "faq_q": "Khung ban ngày của DearSunday có phải tính tiền từng giờ không?",
        "faq_a": "Page giới thiệu khung ban ngày cố định 12:30–20:30 (8 tiếng), không phải gói tính phí từng giờ. Hỏi Page mức phí hiện tại cho ngày bạn muốn đi.",
        "toc": [("Bắt đầu từ việc bạn muốn làm", "muc-tieu"), ("So giờ thực dùng với thời lượng thuê", "thoi-luong"), ("Xác nhận giờ nhận và trả", "nhan-tra"), ("Đừng chỉ so giá ban đầu", "chi-phi")],
        "body": """<p class="lead">Cụm từ <strong>homestay thuê theo giờ Hà Nội</strong> có thể chỉ nhiều cách tính thời gian khác nhau. Có nơi chia theo từng giờ, có nơi bán một khung ban ngày cố định. Trước khi đặt, hãy kiểm tra giờ bắt đầu, giờ kết thúc và tổng thời lượng thực sự có mặt — đừng chỉ dựa vào tên gói.</p>
<h2 id="muc-tieu">Bắt đầu từ việc bạn muốn làm</h2><p>Buổi nghỉ ngắn, một buổi hẹn dài và chuyến qua đêm là ba mục đích khác nhau. Viết ra điều quan trọng nhất: nghỉ ngơi, có không gian riêng, kỷ niệm dịp đặc biệt hay cùng làm một hoạt động. Sau đó chọn nơi và khung giờ đáp ứng mục đích đó.</p><p>Nếu muốn thử vẽ hoặc nấu ăn cùng nhau, cần tính cả thời gian nhận phòng, sắp xếp đồ, làm hoạt động và nghỉ. Nếu chỉ muốn thư giãn, một lịch trình ít điểm dừng có thể hợp hơn.</p>
<h2 id="thoi-luong">So thời gian thực dùng với thời lượng thuê</h2><p>Tính từ lúc dự kiến đến nơi đến lúc cần rời đi. Cộng thêm thời gian đi lại, ăn uống và khoảng đệm trước giờ trả phòng. Nếu khung thuê vừa khít trên giấy, chỉ một chặng đường trễ cũng có thể làm buổi hẹn bị gấp.</p><p>DearSunday giới thiệu khung ban ngày cố định 12:30–20:30, tổng cộng 8 tiếng; đây không phải giá theo từng giờ. Page cũng có khung qua đêm 14:00–11:00 hôm sau và mục “Chỉ ở đêm” 22:00–11:00. Hãy nhắn Page kiểm tra khung phù hợp và lịch còn trống.</p>
<h2 id="nhan-tra">Xác nhận giờ nhận phòng và trả phòng</h2><p>Hỏi rõ thời điểm bắt đầu tính giờ, cách nhận hướng dẫn vào nơi ở, giờ kết thúc và quy trình trả phòng. Nếu có khả năng đến trễ, hỏi trước cách xử lý; đừng mặc định giờ trả phòng được lùi theo giờ đến. Lưu thông tin xác nhận trong cùng một cuộc trò chuyện để dễ xem lại.</p>
<h2 id="chi-phi">Đừng chỉ so giá ban đầu</h2><p>Hãy đề nghị xác nhận tổng chi phí cho đúng ngày và khung giờ, khoản nào đã bao gồm, phí hoạt động nếu có, cách đặt cọc/thanh toán và điều kiện thay đổi hoặc hủy. Giá và dịch vụ có thể tùy ngày hoặc lựa chọn, nên dùng báo giá Page xác nhận thay vì số liệu cũ trên bài viết.</p><div class="callout">Một khung giờ phù hợp là khung bạn có thể tận hưởng thoải mái sau khi đã tính đường đi, giờ nhận-trả và hoạt động dự định.</div><p>DearSunday ở khu vực Triều Khúc, Thanh Xuân. Địa chỉ chi tiết gửi riêng sau khi đặt. Nhắn Page từ khóa <strong>“Sun”</strong> để hỏi lịch và các khoản cần xác nhận.</p>""",
    },
    {
        "slug": "hen-ho-sang-tao-ve-nan-nau", "n": "03", "tag": "Ý TƯỞNG HẸN HÒ · CÙNG SÁNG TẠO",
        "title": "Một buổi hẹn sáng tạo: cùng vẽ, nặn đất sét hay nấu ăn?",
        "desc": "Ba ý tưởng hoạt động dành cho hai người ở Hà Nội: vẽ tranh, nặn đất sét và nấu ăn — cách chọn hoạt động hợp với tính cách và nhịp của buổi hẹn.",
        "image": "room-bedroom-art.webp", "alt": "Tranh và ánh đèn ấm trong một góc phòng DearSunday",
        "faq_q": "Cần có kinh nghiệm mới tham gia hoạt động sáng tạo không?",
        "faq_a": "Những gợi ý trong bài là hoạt động vui vẻ để hai người cùng thử. Hỏi Page về lựa chọn, vật liệu, thời lượng và chi phí áp dụng cho ngày đặt.",
        "toc": [("Chọn hoạt động thay vì cố lên lịch kín", "chon-hoat-dong"), ("Vẽ tranh: cùng nhìn, cùng kể", "ve-tranh"), ("Nặn đất sét: vui cả khi chưa khéo", "nan-dat-set"), ("Nấu ăn: chia việc rồi cùng thưởng thức", "nau-an")],
        "body": """<p class="lead">Một buổi hẹn không nhất thiết phải có thật nhiều điểm đến. Đôi khi một hoạt động nhỏ — vẽ một bức tranh, nặn một món đồ hoặc chuẩn bị món ăn cùng nhau — tạo ra câu chuyện để hai người nhớ lâu hơn. Đây cũng là những lựa chọn trải nghiệm DearSunday giới thiệu tại khu vực Thanh Xuân.</p>
<h2 id="chon-hoat-dong">Chọn hoạt động thay vì cố lên lịch kín</h2><p>Hãy bắt đầu bằng câu hỏi: hai bạn muốn trò chuyện, thử điều mới hay cùng làm ra một món gì đó? Chọn một hoạt động chính là đủ. Chừa thời gian nghỉ và trò chuyện để buổi hẹn không biến thành danh sách việc cần hoàn thành.</p><p>Trước khi đi, nhắn Page xác nhận hoạt động nào còn có, thời lượng, chi phí và vật liệu đã chuẩn bị. Nội dung cung cấp trong gói có thể khác nhau theo lựa chọn; không nên mặc định khi chưa hỏi.</p>
<h2 id="ve-tranh">Vẽ tranh: cùng nhìn, cùng kể</h2><p>Vẽ phù hợp với cặp đôi thích màu sắc hoặc muốn có một vật kỷ niệm. Có thể chọn một chủ đề chung — một nơi muốn đến, món ăn thích nhất hay màu sắc gợi nhớ một ngày vui. Không cần ai có kỹ năng hội họa. Mục tiêu là cùng thử và nhìn cách mỗi người diễn giải một ý tưởng.</p>
<h2 id="nan-dat-set">Nặn đất sét: vui cả khi chưa khéo</h2><p>Chọn một hình đơn giản như chiếc đĩa nhỏ, móc khóa hoặc nhân vật tưởng tượng. Làm cùng một mẫu rồi so sánh hai phiên bản cũng là cách mở đầu câu chuyện. Hãy hỏi trước cách hoàn thiện và nhận lại sản phẩm nếu điều đó quan trọng với hai bạn.</p>
<h2 id="nau-an">Nấu ăn: chia việc rồi cùng thưởng thức</h2><p>Một người có thể chuẩn bị nguyên liệu, người kia sắp xếp bàn hoặc đọc công thức; sau đó đổi vai. Chọn món dễ làm và kiểm tra trước dị ứng, chế độ ăn cùng những dụng cụ có sẵn. Đừng để việc nấu nướng chiếm hết buổi hẹn — một món đơn giản thường khiến cả hai có nhiều thời gian bên nhau hơn.</p><ul class="quick-list"><li>Hỏi Page hoạt động nào có vào ngày đặt</li><li>Xác nhận thời lượng, chi phí và vật liệu</li><li>Báo trước dị ứng hoặc điều cần lưu ý</li><li>Chọn một hoạt động chính, chừa thời gian nghỉ</li></ul><p>DearSunday ở Triều Khúc, Thanh Xuân, dành cho 1–2 người. Nhắn Page từ khóa <strong>“Sun”</strong> để hỏi lịch và lựa chọn hoạt động đang có.</p>""",
    },
    {
        "slug": "lich-hen-ho-ban-ngay-8-tieng", "n": "04", "tag": "BUỔI HẸN BAN NGÀY · 8 TIẾNG",
        "title": "Gợi ý sắp xếp buổi hẹn ban ngày 12:30–20:30",
        "desc": "Lịch trình tham khảo cho buổi hẹn 12:30–20:30 tại DearSunday: đến nơi, nghỉ ngơi, dành thời gian cho một hoạt động đã xác nhận và thu xếp trước giờ trả phòng.",
        "image": "room-reading-corner.webp", "alt": "Góc phòng nghỉ ban ngày với tranh treo tường và chăn vàng tại DearSunday",
        "faq_q": "Khung ban ngày kéo dài bao lâu?",
        "faq_a": "Khung ban ngày DearSunday giới thiệu là 12:30–20:30, tổng cộng 8 tiếng. Lịch trống cần được Page xác nhận.",
        "toc": [("Khung giờ của DearSunday", "khung-dearsunday"), ("Một lịch tham khảo nhẹ nhàng", "lich-tham-khao"), ("Điều chỉnh theo hai bạn", "dieu-chinh"), ("Chuẩn bị trước khi đi", "chuan-bi")],
        "body": """<p class="lead">Nếu hai bạn đang tìm <strong>homestay ban ngày ở Thanh Xuân</strong>, điều đầu tiên nên xem là giờ nhận-trả và tổng thời lượng. DearSunday giới thiệu khung ban ngày 12:30–20:30 (8 tiếng). Bạn có thể xem đây như một khoảng thời gian rộng rãi để nghỉ ngơi và làm điều gì đó cùng nhau — không cần lấp đầy từng phút.</p>
<h2 id="khung-dearsunday">Khung giờ của DearSunday</h2><p>Khung Day Light được giới thiệu là 12:30–20:30. Lịch trống có thể thay đổi theo ngày, vì vậy hãy nhắn Page để xác nhận trước khi lên kế hoạch. Địa chỉ cụ thể được gửi riêng sau khi đặt; tính thời gian di chuyển đến khu vực Triều Khúc, Thanh Xuân trong lịch của mình.</p>
<h2 id="lich-tham-khao">Lịch trình gợi ý theo mốc giờ</h2><p>Đây là cách tự sắp xếp thời gian trong khung 12:30–20:30, không phải lịch hoạt động hay dịch vụ cố định của homestay:</p><ul><li><strong>12:30–13:00:</strong> đến nơi theo hướng dẫn đã nhận, ổn định và nghỉ ngắn.</li><li><strong>13:00–15:00:</strong> dành thời gian trò chuyện, thư giãn hoặc dùng thời gian theo cách hai bạn thích.</li><li><strong>15:00–17:00:</strong> nếu đã xác nhận trước, thử một hoạt động như vẽ, nặn đất sét hoặc nấu ăn; nếu không, tiếp tục nghỉ ngơi.</li><li><strong>17:00–19:30:</strong> để lịch thoáng cho trò chuyện, nghỉ hoặc hoàn tất hoạt động.</li><li><strong>19:30–20:30:</strong> thu xếp đồ dùng và làm thủ tục trả phòng theo hướng dẫn đã xác nhận, trước giờ kết thúc khung.</li></ul><p>Các mốc chỉ để tham khảo; hoạt động và thời lượng thực tế cần được Page xác nhận. Không mặc định có nguyên liệu hay dịch vụ ăn uống.</p>
<h2 id="dieu-chinh">Điều chỉnh theo nhịp của hai bạn</h2><p>Người thích hoạt động có thể chọn một việc cùng làm; người cần nghỉ ngơi có thể bỏ bớt lịch. Để thời gian trống không có nghĩa là lãng phí — đó chính là điều khiến buổi hẹn bớt vội. Nếu dự định tổ chức dịp kỷ niệm, hỏi trước về combo phù hợp, chi phí và những gì cần chuẩn bị.</p>
<h2 id="chuan-bi">Chuẩn bị trước khi đi</h2><p>Xác nhận ngày, khung giờ, số người, tổng chi phí, nội dung hoạt động nếu có, hướng dẫn di chuyển và quy định trả phòng. Lưu lại phản hồi của Page để cả hai cùng xem. Nhắn Page từ khóa <strong>“Sun”</strong> để hỏi lịch ban ngày còn trống.</p><div class="callout">Một buổi hẹn thoải mái không cần lịch trình hoàn hảo. Chỉ cần cả hai cùng thống nhất điều muốn làm và đủ thời gian để tận hưởng nó.</div>""",
    },
    {
        "slug": "homestay-qua-dem-cho-hai-nguoi", "n": "05", "tag": "HOMESTAY QUA ĐÊM · HAI NGƯỜI",
        "title": "Đặt homestay qua đêm cho hai người: 6 điều nên hỏi trước",
        "desc": "Giờ nhận-trả, địa chỉ riêng, tổng chi phí, quy định, dịch vụ và cách xác nhận lịch — 6 điều nên hỏi khi đặt homestay qua đêm cho hai người ở Hà Nội.",
        "image": "room-living-sofa.webp", "alt": "Sofa, bàn trà và cây xanh trong căn phòng riêng của DearSunday",
        "faq_q": "DearSunday nhận phòng qua đêm và trả phòng lúc nào?",
        "faq_a": "Khung qua đêm được giới thiệu là nhận phòng 14:00, trả phòng 11:00 hôm sau. Page còn liệt kê khung “Chỉ ở đêm” 22:00–11:00; hãy xác nhận khung còn trống.",
        "toc": [("Kiểm tra giờ nhận và trả", "gio-nhan-tra"), ("Xác nhận vị trí và cách đến", "vi-tri"), ("Hỏi tổng chi phí", "chi-phi"), ("Làm rõ quy định và lựa chọn thêm", "quy-dinh")],
        "body": """<p class="lead">Khi tìm <strong>homestay qua đêm cho hai người ở Hà Nội</strong>, ảnh đẹp chỉ là một phần quyết định. Giờ nhận-trả, cách nhận địa chỉ, tổng chi phí và quy định của nơi ở mới là thông tin giúp chuyến đi diễn ra đúng kế hoạch. Dưới đây là sáu điều nên xác nhận trực tiếp trước khi đặt.</p>
<h2 id="gio-nhan-tra">1. Giờ nhận phòng và trả phòng là mấy giờ?</h2><p>DearSunday giới thiệu khung qua đêm nhận phòng 14:00, trả phòng 11:00 hôm sau. Page cũng có lựa chọn “Chỉ ở đêm” 22:00–11:00 hôm sau. Hãy xác nhận loại khung đang còn, ngày cụ thể và giờ áp dụng cho đặt chỗ của bạn.</p>
<h2 id="vi-tri">2. Địa chỉ và hướng dẫn đến nơi được gửi thế nào?</h2><p>DearSunday ở khu vực Triều Khúc, Thanh Xuân; địa chỉ cụ thể được gửi riêng sau khi đặt. Trước khi xác nhận, hỏi thời điểm nhận hướng dẫn, cách di chuyển và đầu mối liên hệ nếu cần hỗ trợ. Giữ thông tin địa chỉ trong tin nhắn riêng, không đăng lại công khai.</p>
<h2 id="chi-phi">3. Tổng chi phí và cách thanh toán ra sao?</h2><p>Nhờ Page xác nhận giá cuối cùng cho ngày và khung giờ đã chọn, khoản nào đã bao gồm, phương thức thanh toán, tiền cọc nếu có và điều kiện hoàn/đổi. Giá có thể thay đổi theo ngày hoặc lựa chọn; hãy căn cứ vào thông tin Page gửi cho lịch cụ thể, không dựa vào giá cũ trên bài viết.</p>
<h2 id="quy-dinh">4. Quy định tại homestay là gì?</h2><p>Hỏi về số người được lưu trú, giờ yên tĩnh, việc mang đồ ăn/thức uống, khách đến cùng và quy trình trả phòng. Chỉ cần hỏi những điều liên quan đến kế hoạch của mình, rồi đọc lại hướng dẫn trước khi xác nhận.</p><h3>5. Có lựa chọn trải nghiệm nào?</h3><p>Nếu muốn thêm vẽ, nặn đất sét, nấu ăn hoặc combo kỷ niệm, hỏi xem lựa chọn nào có vào ngày đó, mức phí, thời lượng và cần chuẩn bị gì. Không phải hoạt động nào cũng mặc định bao gồm trong khung nghỉ.</p><h3>6. Khi nào lịch được giữ chỗ?</h3><p>Hỏi bước xác nhận đặt, thời hạn thanh toán nếu có và cách nhận thông báo cuối cùng. Chỉ xem lịch là chắc chắn khi Page xác nhận rõ trạng thái đặt chỗ.</p>
<ul class="quick-list"><li>Ngày lưu trú và khung qua đêm/ở đêm</li><li>Giờ nhận-trả và địa chỉ gửi riêng</li><li>Tổng chi phí, cách thanh toán, điều kiện đổi/hủy</li><li>Quy định và dịch vụ muốn thêm</li></ul><p>DearSunday dành cho 1–2 người tại Triều Khúc, Thanh Xuân. Nhắn Page từ khóa <strong>“Sun”</strong> để hỏi lịch; mọi chi tiết cụ thể cần được Page xác nhận.</p>""",
    },
    {
        "slug": "cau-hoi-truoc-khi-dat-homestay-rieng-tu", "n": "06", "tag": "CHECKLIST ĐẶT PHÒNG · PRIVATE HOMESTAY",
        "title": "Những câu hỏi nên xác nhận trước khi đặt homestay riêng tư",
        "desc": "Checklist đặt private homestay: xác nhận số người, khung giờ, cách nhận địa chỉ riêng, tổng phí, hoạt động và quy định trước khi chốt lịch.",
        "image": "room-cozy-details.webp", "alt": "Một góc trang trí nhỏ trong không gian private homestay DearSunday",
        "faq_q": "Địa chỉ cụ thể của homestay được gửi khi nào?",
        "faq_a": "DearSunday cho biết địa chỉ chi tiết được gửi riêng sau khi đặt. Trước đó, bạn có thể hỏi khu vực chung và cách nhận hướng dẫn qua Page.",
        "toc": [("Thông tin lịch và số khách", "lich-va-so-khach"), ("Riêng tư và địa chỉ", "dia-chi"), ("Giá, dịch vụ và điều kiện", "gia-va-dich-vu"), ("Tin nhắn mẫu để hỏi lịch", "tin-nhan-mau")],
        "body": """<p class="lead">Đặt một <strong>private homestay</strong> thường cần thêm vài xác nhận để cả hai hiểu giống nhau về lịch, vị trí và dịch vụ. Dùng checklist dưới đây để hỏi rõ ngay từ đầu, tránh phải đoán thông tin hoặc thay đổi kế hoạch sát giờ.</p>
<h2 id="lich-va-so-khach">Thông tin lịch và số khách</h2><ul><li>Ngày nào còn trống và khung giờ chính xác là gì?</li><li>Khung tính từ lúc nhận phòng đến giờ nào? Có cần trả đúng giờ không?</li><li>Số khách tối đa và quy định đăng ký khách thế nào?</li><li>Điều gì xác nhận lịch đã được giữ?</li></ul><p>DearSunday phù hợp cho 1–2 người; khung ban ngày được giới thiệu là 12:30–20:30, khung qua đêm 14:00–11:00 hôm sau và lựa chọn “Chỉ ở đêm” 22:00–11:00 hôm sau. Hỏi Page về ngày cụ thể vì tình trạng trống thay đổi.</p>
<h2 id="dia-chi">Riêng tư và địa chỉ được gửi ra sao?</h2><p>Hỏi khu vực chung trước để tính đường đi; hỏi thời điểm nhận địa chỉ chính xác và hướng dẫn đến nơi. DearSunday ở khu vực Triều Khúc, Thanh Xuân, Hà Nội; địa chỉ cụ thể gửi riêng sau khi đặt. Không cần xin vị trí nhà trong bình luận công khai, cũng không nên chia sẻ lại địa chỉ riêng tư khi chưa được cho phép.</p>
<h2 id="gia-va-dich-vu">Giá, hoạt động và điều kiện</h2><p>Xác nhận tổng chi phí cho ngày/khung giờ đã chọn, những khoản đã gồm, phương thức thanh toán, điều kiện thay đổi hoặc hủy và quy định sử dụng phòng. Nếu muốn hoạt động vẽ, nặn đất sét, nấu ăn hoặc combo kỷ niệm, hỏi lựa chọn nào có, chi phí nếu có, thời lượng và vật liệu chuẩn bị. Chờ Page xác nhận thay vì suy đoán từ ảnh hoặc bài cũ.</p><h3>Cách ghi lại xác nhận</h3><p>Sau khi hai bên thống nhất, lưu một tin nhắn có ngày, khung giờ, số người, tổng phí, bước thanh toán và trạng thái đặt. Nếu có thay đổi, hỏi lại bằng văn bản để thông tin không bị sót.</p>
<h2 id="tin-nhan-mau">Tin nhắn mẫu để hỏi lịch</h2><div class="callout">“Chào DearSunday, mình muốn hỏi lịch ngày [ngày] cho [số người], khung [ban ngày/qua đêm]. Cho mình xin tổng chi phí, thông tin hoạt động [nếu muốn], cách xác nhận đặt và hướng dẫn nhận địa chỉ riêng nhé.”</div><p>Tin nhắn càng cụ thể thì Page càng dễ kiểm tra lịch và trả lời đúng nhu cầu. Với DearSunday, có thể gửi từ khóa <strong>“Sun”</strong> để hỏi lịch trống.</p>""",
    },
]

for index, a in enumerate(ARTICLES):
    toc = "".join(f'<li><a href="#{anchor}">{escape(title)}</a></li>' for title, anchor in a["toc"])
    related = [ARTICLES[(index + offset) % len(ARTICLES)] for offset in (1, 2, 3)]
    related_html = "".join(f'<a href="{escape(item["slug"])}.html"><small>GUIDE {item["n"]} · {escape(item["tag"])}</small><strong>{escape(item["title"])}</strong></a>' for item in related)
    words = len(re.sub(r"<[^>]+>", " ", a["body"]).split())
    faq_extra_html = "".join(f'<details><summary>{escape(question)}</summary><p>{escape(answer)}</p></details>' for question, answer in a.get("faq_extra", []))
    reading_minutes = max(1, (words + 159) // 160)
    ld = {"@context":"https://schema.org","@type":"BlogPosting","headline":a["title"],"description":a["desc"],"wordCount":words,"datePublished":"2026-10-31","dateModified":a.get("modified", "2026-10-31"),"inLanguage":"vi","author":{"@type":"Organization","name":"Cẩm nang DearSunday"},"publisher":{"@type":"Organization","name":"DearSunday","sameAs":PAGE}}
    breadcrumb_ld = {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Trang chủ","item":SITE},{"@type":"ListItem","position":2,"name":"Cẩm nang","item":SITE+"#bai-viet"},{"@type":"ListItem","position":3,"name":a["tag"].title()}]}
    page = f'''<!doctype html>
<html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="{escape(a['desc'], quote=True)}"><meta name="robots" content="index,follow,max-image-preview:large"><meta name="theme-color" content="#f8f6f2"><title>{escape(a['title'])} | {escape(a.get('title_suffix', 'Cẩm nang DearSunday'))}</title><link rel="icon" href="../favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="../styles.css"><script type="application/ld+json">{json.dumps(ld, ensure_ascii=False, separators=(',', ':'))}</script><script type="application/ld+json">{json.dumps(breadcrumb_ld, ensure_ascii=False, separators=(',', ':'))}</script></head>
<body><header class="header shell"><a class="brand" href="../index.html">Dear<span>Sunday</span><i>Journal</i></a><nav class="nav" aria-label="Điều hướng chính"><a class="active" href="../index.html">Cẩm nang</a><a href="../about.html">Về DearSunday</a></nav><a class="header-cta" href="{PAGE}" target="_blank" rel="noopener noreferrer">Hỏi lịch <span>↗</span></a></header>
<main><div class="breadcrumbs shell"><a href="../index.html">Trang chủ</a><span>›</span><a href="../index.html#bai-viet">Cẩm nang</a><span>›</span>{escape(a['tag'].title())}</div>
<section class="article-hero"><p class="article-kicker">{escape(a['tag'])}</p><h1>{escape(a['title'])}</h1><p class="article-deck">{escape(a['desc'])}</p><p class="article-meta">CẨM NANG DEARSUNDAY &nbsp; · &nbsp; {a['n']} / 06 &nbsp; · &nbsp; {reading_minutes} PHÚT ĐỌC</p></section>
<img class="article-cover" src="../images/{escape(a['image'], quote=True)}" alt="{escape(a['alt'], quote=True)}" fetchpriority="high"><p class="cover-caption">Ảnh không gian DearSunday · Triều Khúc, Thanh Xuân</p>
<div class="article-layout"><aside class="article-aside"><strong>TRONG BÀI NÀY</strong><ul>{toc}</ul><a class="aside-cta" href="{PAGE}" target="_blank" rel="noopener noreferrer"><b>Hỏi lịch DearSunday ↗</b>Địa chỉ chi tiết được gửi riêng sau khi đặt.</a></aside><article class="prose">{a['body']}<div class="faq-block"><h2 id="faq">Câu hỏi thường gặp</h2><details><summary>{escape(a['faq_q'])}</summary><p>{escape(a['faq_a'])}</p></details>{faq_extra_html}</div><div class="cta-box"><strong>Một ngày của hai bạn, theo cách riêng.</strong><p>Nhắn Page DearSunday để hỏi lịch trống và xác nhận thông tin mới nhất.</p><a href="{PAGE}" target="_blank" rel="noopener noreferrer">NHẮN DEARSUNDAY ↗</a></div></article></div>
<section class="related"><div class="shell"><p>KEEP READING</p><h2>Đọc thêm từ Cẩm nang.</h2><div class="related-links">{related_html}</div></div></section></main>
<footer class="footer shell"><a class="brand" href="../index.html">Dear<span>Sunday</span><i>Journal</i></a><span>TRIỀU KHÚC · THANH XUÂN · HÀ NỘI</span><a href="{PAGE}" target="_blank" rel="noopener noreferrer">Facebook DearSunday ↗</a><small>© 2026 DearSunday Journal</small></footer></body></html>'''
    (ROOT / "blog" / f"{a['slug']}.html").write_text(page, encoding="utf-8")

print(f"Wrote {len(ARTICLES)} blog articles")
